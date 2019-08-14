import numpy as np 
import numpy.matlib 
from numpy import linalg as LA
import matplotlib.pyplot as plt 
import json
import os.path
from os import path

# X=A−(1/n).e.eT.A

# E = np.matlib.ones((1000,1000))*0.001
# X1 = E.dot(A)
# X = np.subtract(A,X1)
# Y=X.dot(X.transpose())

x_avg = 0
y_avg = 0

x_dot = []
y_dot = []

if path.isfile('data.json'):
    with open('data.json', 'r') as f:
        scatter = json.load(f)
        x_dot=scatter['x']
        y_dot=scatter['y']

def generate():
    A = np.matlib.rand(1000,2)    
    for i in range(0,1000):
        x_dot.append(A[i,0])
        y_dot.append(A[i,1])
    with open('data.json','w') as f:
        data = {
                "x": x_dot,
                "y": y_dot
            }
        json.dump(data,f)
    
def calculate():
    A = np.matlib.empty((2,1000),dtype=float) 
    for i in range(0,1000):
        A[0,i] = x_dot[i] 
        A[1,i] = y_dot[i]
    C = np.cov(A)
    Mu = np.mean(A,axis=1)
    print(Mu)
    print(C)
    lambdaval ,lambdavec = LA.eig(C)
    print(lambdavec)
    print(lambdaval)
    plt.scatter(x_dot,y_dot)
    plt.quiver(Mu[0,0],Mu[1,0],lambdavec[0,:],lambdavec[1,:],color=['r','g'])
    plt.show()

def main():
    generate()
    calculate()

if __name__=='__main__':
    main()