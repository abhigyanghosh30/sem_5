#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix 
import csv

data = []
labels = []

test_data = []
test_labels = []

with open('sample_train.csv','r') as f:
    rows = csv.reader(f)
    for row in rows:
        data.append(row[1:])
        labels.append(int(row[0]))


with open('sample_test.csv','r') as f:
    rows = csv.reader(f)
    for row in rows:
        test_data.append(row[1:])
        test_labels.append(int(row[0]))
        
test_data = np.matrix(test_data).astype(int)


# In[59]:


model_dict = {}
for i in range(10):
    for j in range(i):
        model_data = []
        model_labels = []
        for k in range(len(labels)):
            if(labels[k]==i):
                model_data.append(data[k])
                model_labels.append(1)
            if(labels[k]==j):
                model_data.append(data[k])
                model_labels.append(-1)
        model_dict[str(i)+str(j)]  = LogisticRegression(random_state=0, solver='lbfgs',max_iter=1000,multi_class='multinomial').fit(model_data, model_labels)


# In[83]:


accuracy = 0
y_predicted = []
for label in range(len(test_labels)):
    votes = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        for j in range(i):
            temp = test_data[label,:].reshape(1,-1)
            pred = model_dict[str(i)+str(j)].predict(temp)
            if(pred[0]==1):
                votes[i]+=1
            else:
                votes[j]+=1
    indices = np.argsort(votes)
    if(test_labels[label] == indices[-1]):
        accuracy += 1
    y_predicted.append(indices[-1])
    


# In[86]:


print(accuracy/len(test_labels)*100)
print(confusion_matrix(test_labels, y_predicted))


# In[ ]:




