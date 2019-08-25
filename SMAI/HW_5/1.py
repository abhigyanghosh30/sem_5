import numpy as np
import matplotlib.pyplot as plt 
import os

if os.path.isfile('data_A.npy'):
    A = np.load('data_A.npy')

if os.path.isfile('data_B.npy'):
    B = np.load('data_B.npy')

def generate():
    mean_1 = [3,3]
    mean_2 = [7,7]
    cov_1 = cov_2 = [[3,0],[0,3]]
    A = np.random.multivariate_normal(mean_1, cov_1, 1000)
    B = np.random.multivariate_normal(mean_2, cov_2, 1000)
    np.save('data_A.npy',A)
    np.save('data_B.npy',B)
