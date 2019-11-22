#!/usr/bin/env python
# coding: utf-8

# In[35]:


from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
x1 = np.random.normal(-1,1,(5,2))
x2 = np.random.normal(1,1,(5,2))
l1 = np.zeros(5)
l2 = np.ones(5)
X = np.vstack((x1,x2))
labels = np.hstack((l1,l2))
print(x1.shape)
print(x2.shape)
print(X.shape)
kmeans = KMeans(n_clusters=2).fit(X)
fig = plt.figure(figsize=(24,8))
ax = fig.add_subplot(121)
ax.set_title('K-Means Output')
ax.scatter(X[:,0],X[:,1],c=kmeans.labels_)
ax = fig.add_subplot(122)
ax.set_title('Ground Truth Plot')
ax.scatter(X[:,0],X[:,1],c=labels)


# In[38]:


fig = plt.figure(figsize=(24,8))
ax = fig.add_subplot(111)
inertias = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i).fit(X)
    inertias.append(kmeans.inertia_)
    print("k=",i,"Iterations=",kmeans.n_iter_)
    print("Labels=",kmeans.labels_)
ax.set_title('Inertia vs k')
ax.plot(inertias)
plt.show()


# In[ ]:




