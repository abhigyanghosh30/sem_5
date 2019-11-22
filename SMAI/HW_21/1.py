#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np 
from sklearn.cluster import KMeans
X = np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
kmeans = KMeans(n_clusters=2, init=np.asarray([[0, 0], [0, 0]]), n_init=1).fit(X)
print("Iterations#",kmeans.n_iter_)
print("Final Labels: [%d,%d,%d,%d]"%tuple(kmeans.labels_))


# In[8]:


for i in range(3):
    kmeans = KMeans(n_clusters=2, init=np.asarray([[0, 0], [0, 0]]), n_init=1, max_iter=i+1).fit(X)
    print("Iteration #%d"%(i+1))
    print("labels [%d,%d,%d,%d]"%tuple(kmeans.labels_))
    print("Interita:",kmeans.inertia_)


# In[ ]:




