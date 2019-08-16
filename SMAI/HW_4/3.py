import os
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


if os.path.isfile('data_A.npy'):
    A = np.load('data_A.npy')

if os.path.isfile('data_B.npy'):
    B = np.load('data_B.npy')


def generate():
    mean_a = [0, 0, 0]
    mean_b = [2, 2, 2]
    cov_a = cov_b = np.dot([[1,2,3],[2,3,4],[3,2,1]],np.transpose([[1,2,3],[2,3,4],[3,2,1]]))
    print(cov_a)
    A = np.random.multivariate_normal(mean_a, cov_a, 1000)
    B = np.random.multivariate_normal(mean_b, cov_b, 1000)
    np.save('data_A.npy',A)
    np.save('data_B.npy',B)


def plot():
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d') # comment out for 2D 
    plt.scatter(np.array(A[:,1]),np.array(A[:,2]),color='r',marker='o')
    plt.scatter(np.array(B[:,1]),np.array(B[:,2]),color='b',marker='x')
    plt.xlabel('Y Axis')
    plt.ylabel('Z Axis')
    # plt.set_zlabel('Z Axis')
    plt.show()

if __name__ == "__main__":
    # generate()
    plot()
