import numpy as np
import matplotlib.pyplot as plt 

w1 = np.matrix('0 0; 0 1; 2 0; 3 2; 3 3; 2 2; 2 0')
w2 = np.matrix('7 7; 8 6; 9 7; 8 10; 7 10; 8 9; 7 11')

m1 = np.mean(w1,axis=0)
m2 = np.mean(w2,axis=0)
print("Mean")
print(m1)
print(m2)
print()
cov1 = np.cov(w1.T)
cov2 = np.cov(w2.T)

print("Covariance")
print(cov1)
print(cov2)

cov1_inv = np.linalg.inv(cov1)
cov2_inv = np.linalg.inv(cov2)
print("Covariance Inverse")
print(np.linalg.inv(cov1))
print(np.linalg.inv(cov2))
print("Covariance Determinant")
print(np.log(np.linalg.det(cov1)))
print(np.log(np.linalg.det(cov2)))


x = np.linspace(-5, 15, 400)
y = np.linspace(-5, 15, 400)
x, y = np.meshgrid(x, y)

# plt.contour(x,y,(x*x+y*y+x*y),[0],colors='k')

x_1 = []
y_1 = []
x_2 = []
y_2 = []
for i in range(7):
    x_1.append(w1[i,0])
    y_1.append(w1[i,1])
    y_2.append(w2[i,1])
    x_2.append(w2[i,0])
plt.scatter(x_1,y_1,c='g')
plt.scatter(x_2,y_2,c='b')
plt.contour(x,y,(1.23075216*x*x-38.42858464*x+1.91836659*x*y-11.54348912*y-0.67267112*y*y+204.9249634),[0],colors='k')
plt.contour(x,y,(1.23075216*x*x-38.42858464*x+1.91836659*x*y-11.54348912*y-0.67267112*y*y+204.9249634+np.log(4)),[0],colors='y')
plt.show()