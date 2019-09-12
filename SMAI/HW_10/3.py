#!/usr/bin/env python
# coding: utf-8

# In[215]:


import numpy as np
import pickle
from matplotlib import pyplot as plt
import matplotlib.cm as cm


def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

data1 = unpickle('cifar-10-batches-py/data_batch_1')
data2 = unpickle('cifar-10-batches-py/data_batch_2')
data3 = unpickle('cifar-10-batches-py/data_batch_3')
data4 = unpickle('cifar-10-batches-py/data_batch_4')
data5 = unpickle('cifar-10-batches-py/data_batch_5')
data = np.vstack((data1[b'data'],data2[b'data'],data3[b'data'],data4[b'data'],data5[b'data']))
labels = np.vstack((data1[b'labels'],data2[b'labels'],data3[b'labels'],data4[b'labels'],data5[b'labels']))
labels = labels.flatten()


# conversion to greyscale
data = data/255;
data = 0.299 * data[:,:1024] + 0.587 * data[:,1024:2048] + 0.114 * data[:,2048:3072]
print(data.shape)


# In[216]:


indices = np.argsort(labels)
data = data[indices]
labels = labels[indices]

means=[]
for i in range(0,50000,5000):
    means.append(np.mean(data[i:i+5000],axis=0))
print(np.matrix(means).shape)
print(means)


# In[217]:


class_vectors = []
for i in range(0,50000,5000):
    values,vectors = np.linalg.eig(np.cov(data[i:i+5000].T))

    indices = np.argsort(values)
    indices = np.flip(indices)
    vectors = vectors[indices]
    values = values[indices]
    class_vectors.append(vectors[:,:20])
print(np.shape(class_vectors))
print(class_vectors)


# In[218]:


red_data = (np.matmul(data[0:5000],class_vectors[0]))
print(np.shape(red_data))
for i in range(1,10):
    red_data = np.vstack((red_data,np.dot(data[i*5000:(i+1)*5000],class_vectors[i])))
print(np.shape(red_data))
plt.show()

# In[219]:


rec_data = (np.dot(red_data[0:5000],class_vectors[0].T))
print(np.shape(rec_data))
for i in range(1,10):
    rec_data = np.vstack((rec_data,np.dot(red_data[i*5000:(i+1)*5000],class_vectors[i].T)))
print(np.shape(rec_data))


er_data = np.sqrt(np.sum(np.square(rec_data-data),axis=1))
print(er_data.shape)
errors = []
for i in range(10):
    errors.append(np.sum(er_data[i*5000:(i+1)*5000])/5000)
plt.bar([i for i in range(len(errors))],errors)
print(errors)


# In[220]:


red_means=[np.mean(red_data[0:5000],axis=0)]
for i in range(5000,50000,5000):
    red_means.append(np.mean(red_data[i:i+5000],axis=0))
print(np.matrix(red_means).shape)

split_red_data = np.split(red_data,10)
print(np.matrix(split_red_data[0]).shape)

for i in range(10):
     print(np.sum(np.square(split_red_data[i]-red_means[i])))


# In[225]:


for i in range(10):
    for j in range(10):
        print(np.sqrt(np.sum(np.square(means[i]-means[j]))),end="\t")
    
    


# In[222]:


errors = np.empty([10,10])
for i in range(10):
    for j in range(10):
        Eab = np.sum(np.square((means[i]+rec_data[j*5000:(j+1)*5000])-data[i*5000:(i+1)*5000]),axis=1)/1024 
        Eba = np.sum(np.square((means[j]+rec_data[i*5000:(i+1)*5000])-data[j*5000:(j+1)*5000]),axis=1)/1024
        errors[i][j]=(np.sum(Eab)+np.sum(Eba)/2)
print(errors)


# In[223]:


for i in range(10):
    indices = np.argsort(errors[i])
    print(indices[0:4])

plt.show()


