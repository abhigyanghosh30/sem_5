#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv
import numpy as np
from matplotlib import pyplot as plt


data_rows=[]
data_labels=[]
with open('wine.data','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        data_rows.append(row[1:])
        data_labels.append(row[0])
data_rows = np.matrix(data_rows).astype(np.float) 


# In[33]:


cov = np.cov(data_rows.T)
print(cov.shape)
print(cov)


# In[36]:


mean = np.mean(data_rows,axis=0)
print(mean.shape)
data_rows = data_rows - mean
print(data_rows.shape)
# std_dev.reshape((13,1))
# std_dev = np.diag(std_dev.T)
std_dev = np.sqrt(np.diag(np.diag(cov)))
print(std_dev.shape)
data_rows = np.matmul(data_rows,np.linalg.inv(std_dev))


# In[38]:


cov = np.cov(data_rows.T)
print(cov.shape)
print(cov)
values,vectors = np.linalg.eig(cov)
index = np.argsort(values)
values = values[index]
vectors = vectors[index]
print(values)
fig1 = plt.figure()
p1 = fig1.add_subplot(111,title='Eigenvalues Plot')
p1.scatter([i for i in range(len(values))],values)


# In[54]:


red_data = np.dot(vectors[11:13],data_rows.T)
red_data = np.matrix(red_data)


# In[56]:


fig2 = plt.figure()
p2 = fig2.add_subplot(111,title='Scatter')
p2.scatter(np.array(red_data[0,:59]),np.array(red_data[1,:59]),c='r')
p2.scatter(np.array(red_data[0,59:131]),np.array(red_data[1,59:131]),c='y')
p2.scatter(np.array(red_data[0,131:]),np.array(red_data[1,131:]),c='b')

plt.show()

# In[ ]:




