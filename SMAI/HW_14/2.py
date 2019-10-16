#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
from matplotlib import pyplot as plt

data_a = np.random.normal(-1,1,1000)
data_b = np.random.normal(1,1,1000)
# plt.bar([i for i in range(1000)],data_a,color='r')
# plt.bar([i for i in range(1000)],data_b,color='b')


# In[11]:


def MSE(w):
    func = []
    for i in range(len(w)):
        error = 0
        for j in range(1000):
            error += (-1-w[i]*data_a[j]) * (-1-w[i]*data_a[j])
            error += (1-w[i]*data_b[j]) * (1-w[i]*data_b[j])
        func.append(error)
    return func

def g(x):
    return 1/(1+ np.exp(x))

def LR(w):
    func = []
    for i in range(len(w)):
        error = 0
        for j in range(1000):
            error += (-1-g(w[i]*data_a[j])) * (-1-g(w[i]*data_a[j]))
            error += (1-g(w[i]*data_b[j])) * (1-g(w[i]*data_b[j]))
        func.append(error)
    return func



w = np.linspace(-100,100,1000)
cost = MSE(w)
plt.plot(w,cost)


# In[12]:


cost = LR(w)
plt.plot(w,cost)


# In[ ]:




