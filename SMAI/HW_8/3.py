from matplotlib import pyplot as plt
import numpy as np
data = np.matrix('2 1;2 -1;-2 1;-2 -1')
mean = np.mean(data,axis=0)
cov = np.cov(data.T)
values,vectors = np.linalg.eig(cov)
vectors = vectors*values

print(vectors)

# print(data[:,1])
# print(mean[0])

plt.scatter(np.array(data[:,0]),np.array(data[:,1]),c='b')
plt.scatter(mean[0,0],mean[0,1],c='r')
plt.quiver(mean[0,0],mean[0,1],vectors[:,0],vectors[:,1],color=['r','g'])
plt.show()