#!/usr/bin/env python
# coding: utf-8

# In[71]:


import torch
import torch.nn as nn
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torch.nn.init as weight_init
import matplotlib.pyplot as plt
import pdb
import torch.nn.functional as F


#parameters
batch_size = 128

preprocess = transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])

#Loading the train set file
dataset = datasets.MNIST(root='./data',
                            transform=preprocess,  
                            download=True)

loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)


# In[72]:


class AE(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 256),
            nn.ReLU(),
            nn.Linear(256,64),
            nn.ReLU(),
            nn.Linear(64,20),
        )
        self.decoder = nn.Sequential(
            nn.Linear(20, 64),
            nn.ReLU(),
            nn.Linear(64, 256),
            nn.ReLU(),
            nn.Linear(256, 28*28),
            nn.Tanh()
        )
    
    def forward(self,x):
        h = self.encoder(x)
        xr = self.decoder(h)
        return xr,h


# In[73]:


use_cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if use_cuda else "cpu")
criterion = nn.MSELoss()
learning_rate = 1e-2
weight_decay = 1e-5
net = AE()
net = net.to(device)
optimizer = torch.optim.RMSprop(net.parameters(), lr=learning_rate, weight_decay=weight_decay)


# In[74]:


#Training
def train(num_epochs = 50):
    epochLoss = []
    for epoch in range(num_epochs):
        total_loss, cntr = 0, 0

        for i,(images,_) in enumerate(loader):

            images = images.view(-1, 28*28)
            images = images.to(device)

            # Initialize gradients to 0
            optimizer.zero_grad()

            # Forward pass (this calls the "forward" function within Net)
            outputs, _ = net(images)

            # Find the loss
            loss = criterion(outputs, images)

            # Find the gradients of all weights using the loss
            loss.backward()

            # Update the weights using the optimizer and scheduler
            optimizer.step()

            total_loss += loss.item()
            cntr += 1

    #     scheduler.step(total_loss/cntr)
        print ('Epoch [%d/%d], Loss: %.4f' 
                       %(epoch+1, num_epochs, total_loss/cntr))
        epochLoss.append(total_loss/cntr)
    return epochLoss


# In[76]:


train()


# In[91]:


class FullNet(nn.Module):
    def __init__(self):
        super(FullNet, self).__init__()
        self.fc1 = nn.Linear(784, 320)
        self.fc2 = nn.Linear(320, 50)
        self.fc3 = nn.Linear(50, 10)
    
    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.softmax(x,dim=1)

class RedNet(nn.Module):
    def __init__(self):
        super(RedNet, self).__init__()
        self.fc1 = nn.Linear(20, 15)
        self.fc2 = nn.Linear(15, 12)
        self.fc3 = nn.Linear(12, 10)
    
    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.softmax(x,dim=1)


# In[92]:


fnet = FullNet()
fnet.to(device)
rnet = RedNet()
rnet.to(device)

optimizer_fnet = torch.optim.SGD(fnet.parameters(), lr=learning_rate)
optimizer_rnet = torch.optim.SGD(rnet.parameters(), lr=learning_rate)
criterion_fnet = nn.CrossEntropyLoss()
criterion_rnet = nn.CrossEntropyLoss()


# In[99]:


def train_full(num_epochs = 50):
    epochLoss = []
    for epoch in range(num_epochs):
        total_loss, cntr = 0, 0

        for i,(images,labels) in enumerate(loader):

            images = images.view(-1, 28*28)
            images,labels = images.to(device),labels.to(device)

            # Initialize gradients to 0
            optimizer_fnet.zero_grad()

            # Forward pass (this calls the "forward" function within Net)
            full, red = net(images)
            out_fnet = fnet(full)
            
            # Find the loss
            loss_full = criterion_fnet(out_fnet,labels)
            
            # Find the gradients of all weights using the loss
            loss_full.backward()
            
            # Update the weights using the optimizer and scheduler
            optimizer_fnet.step()
            
            total_loss += loss_full.item()
            cntr += 1

    #     scheduler.step(total_loss/cntr)
        print ('Epoch [%d/%d], Loss: %.4f' 
                       %(epoch+1, num_epochs, total_loss/cntr))
        epochLoss.append(total_loss/cntr)
    return epochLoss


# In[100]:


train_full()


# In[103]:


def train_red(num_epochs = 50):
    epochLoss = []
    for epoch in range(num_epochs):
        total_loss, cntr = 0, 0

        for i,(images,labels) in enumerate(loader):

            images = images.view(-1, 28*28)
            images,labels = images.to(device),labels.to(device)

            # Initialize gradients to 0
            optimizer_rnet.zero_grad()

            # Forward pass (this calls the "forward" function within Net)
            full, red = net(images)
            out_rnet = rnet(red)
            
            # Find the loss
            loss_red = criterion_rnet(out_rnet,labels)
            
            # Find the gradients of all weights using the loss
            loss_red.backward()
            
            # Update the weights using the optimizer and scheduler
            optimizer_rnet.step()
            
            total_loss += loss_red.item()
            cntr += 1

    #     scheduler.step(total_loss/cntr)
        print ('Epoch [%d/%d], Loss: %.4f' 
                       %(epoch+1, num_epochs, total_loss/cntr))
        epochLoss.append(total_loss/cntr)
    return epochLoss


# In[104]:


train_red()


# In[113]:


test_loader = torch.utils.data.DataLoader(
  torchvision.datasets.MNIST('./data', train=False, download=True,
                             transform=torchvision.transforms.Compose([
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])),
  batch_size=batch_size, shuffle=True)

correct_red = [0 for i in range(10)]
correct_full = [0 for i in range(10)]
total = [0 for i in range(10)]
with torch.no_grad():
    for i,(images,labels) in enumerate(test_loader):
        images = images.view(-1, 28*28)
        images,labels = images.to(device),labels.to(device)
        full, red = net(images)
        out_rnet = rnet(red)
        out_fnet = fnet(full)
        _, predicted_full = torch.max(out_fnet.data, 1)

        c_full = (predicted_full == labels).squeeze()
        _, predicted_red = torch.max(out_rnet.data, 1)

        c_red = (predicted_red == labels).squeeze()
        
        for i in range(len(labels)):
            label = labels[i]
            correct_full[label] += c_full[i].item()
            correct_red[label] += c_red[i].item()
            total[label] += 1
plt.bar([i for i in range(10)],correct_full)
plt.show()
plt.bar([i for i in range(10)],correct_red)
plt.show()


# In[ ]:




