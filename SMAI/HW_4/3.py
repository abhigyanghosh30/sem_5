import os
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


if os.path.isfile('data_3A.npy'):
    A = np.load('data_3A.npy')

if os.path.isfile('data_3B.npy'):
    B = np.load('data_3B.npy')


def generate():
    mean = [0, 0, 0]
    # mean_b = [1, 1, 1]
    cov_a = [[1,2,3],[4,5,6],[7,8,9]]
    cov_b = [[4,0,0],[0,8,0],[0,0,6]]
    A = np.random.multivariate_normal(mean, cov_a, 1000)
    B = np.random.multivariate_normal(mean, cov_b, 1000)
    np.save('data_3A.npy',A)
    np.save('data_3B.npy',B)


def plot():
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d') # comment out for 2D 
    plt.scatter(np.array(A[:,1]),np.array(A[:,2]),color='r',marker='o')
    plt.scatter(np.array(B[:,1]),np.array(B[:,2]),color='b',marker='x')
    plt.xlabel('Y Axis')
    plt.ylabel('Z Axis')
    # ax.set_zlabel('Z Axis')
    plt.show()

if __name__ == "__main__":
    # generate()
    plot()
