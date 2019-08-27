import numpy as np
import matplotlib.pyplot as plt 
import os

if os.path.isfile('data_x.npy'):
    x = np.load('data_x.npy')

if os.path.isfile('data_y.npy'):
    y = np.load('data_y.npy')

def generate():
    x = np.random.uniform(0,10,1000)
    y = np.random.uniform(0,10,1000)
    np.save('data_x.npy',x)
    np.save('data_y.npy',y)


def mahalnobis(mean,sigma,xi):
    var1 = np.dot(xi-mean,np.dot(np.linalg.inv(sigma),np.transpose(xi-mean)))
    numer = np.exp(np.dot(-0.5,var1))
    denom = np.power((np.power(2*np.pi,2)*np.linalg.det(sigma)),0.5)
    return numer/denom

def plot():
    colors = []
    mean_1 = np.matrix([3,3])
    mean_2 = np.matrix([7,7])
    cov_1 = cov_2 = np.matrix([[3,0],[0,3]])
    for i in range(1000):
        xi = np.matrix([x[i],y[i]])
        if mahalnobis(mean_1,cov_1,xi) > mahalnobis(mean_2,cov_2,xi):
            colors.append('r')
        else:
            colors.append('g') 
    # plt.scatter(x,y,c=colors)


    colors = []
    cov_1 = np.matrix([[3,1],[2,3]])
    cov_2 = np.matrix([[7,2],[1,7]])
    for i in range(1000):
        xi = np.matrix([x[i],y[i]])
        if mahalnobis(mean_1,cov_1,xi) > mahalnobis(mean_2,cov_2,xi):
            colors.append('r')
        else:
            colors.append('g') 
    plt.scatter(x,y,c=colors)
    plt.show()

if __name__ == "__main__":
    # generate()
    plot()
