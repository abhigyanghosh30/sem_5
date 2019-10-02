#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

data = [[0, 1, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 0, 1]]

labels = np.array([1,1,-1,-1])


# In[ ]:


print(data)
print(labels)


# In[ ]:


its = 0

def batch_percep(w,n=0.4):

    print(w)

    global its
    its += 1
    if(its>100):
        return [0,0,0]

    errors = []
    
    for i in range(len(data)):
        clas = np.matmul(data[i],w.T)
        if(clas*labels[i]<0):
            errors.append((data[i],labels[i]))
    
    if len(errors) == 0:
        return w

    else:
        w_1=[w[0],w[1],w[2]]
        for i in range(len(errors)):
            w_1[0] += errors[i][0][0] * 2 * n * errors[i][1]
            w_1[1] += errors[i][0][1] * 2 * n * errors[i][1]
            w_1[2] += errors[i][0][2] * 2 * n * errors[i][1]

        return batch_percep(np.array(w_1))    


# In[ ]:


w_percep = (batch_percep(np.array([1,0,0])))


# In[ ]:


its = 0


def sigmoid_activation(w,n=1.5,gamma = 10):
    print(w)
    
    global its
    
    its += 1
    if(its>100):
        return w
    
    y = []
    for i in range(len(labels)):
        y.append((labels[i]+1)/2)
    z = gamma * np.matmul(data, w.T)
    h = (1 / (1 + np.exp(-z)))
    gradient = np.matmul(np.transpose(data), (h - y)) / len(data)
    w = w - n * gradient
    return sigmoid_activation(w)


# In[ ]:


w_sigmoid = (sigmoid_activation(np.array([1,0,0])))


# In[ ]:





# In[ ]:


# margin is min distance in each class. If it is almost equal for all classes, then it is better margin
def get_margin(w):
    distances = np.absolute(np.matmul(data,w))
#     print(distances)
    return np.amin(distances[0,0:2])/(w[0]*w[0]+w[1]*w[1]) - np.amin(distances[0,2:4])/(w[0]*w[0]+w[1]*w[1])

print(get_margin(w_percep))
print(get_margin(w_sigmoid))


# In[ ]:





# In[ ]:




