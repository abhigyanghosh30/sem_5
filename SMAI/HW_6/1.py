import numpy as np 
from matplotlib import pyplot as plt 
from sklearn.model_selection import KFold
import os

if os.path.isfile('data_1_y100.npy'):
    y_100 = np.load('data_1_y100.npy')

if os.path.isfile('data_1_y1000.npy'):
    y_1000 = np.load('data_1_y1000.npy')



def generate():
    x_100 = np.array([ i for i in range(100)])
    x_1000 = np.array([ i for i in range(1000)])

    n_100 = np.random.normal(0,1,100)
    n_1000 = np.random.normal(0,1,1000)

    y_100 = np.sin(x_100) + n_100
    y_1000 = np.sin(x_1000) + n_1000

    np.save('data_1_y1000.npy',y_1000)
    np.save('data_1_y100.npy',y_100)

def calculate():
    folds = [1,2,5,10,20,25,50]
    mean_var_100 = []
    for fold in folds:
        kf = KFold(fold,True,1)
        

if __name__ == "__main__":
    generate()
    calculate()