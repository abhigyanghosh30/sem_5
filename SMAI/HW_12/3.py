import numpy as np
from matplotlib import pyplot as pyplot

def cost_MSE():
    cost = 0
    for i in range(1000):
        cost += np.square(self.t1 * x[i] + self.t2 - y[i])
    return cost/2000

def dev_MSE():
    s1 = s2 = 0
    for j in range(1000):
        s1 += x[j]*(self.t1 * x[j] + self.t2 - y[j])
        s2 += (self.t1 * x[j] + self.t2 - y[j])
    return s1/1000,s2/1000

def gradient_descent(n=0.01,iterations=1000):
    costs = []
    t1s = []
    t2s = []
    for i in range(iterations):
        costs.append(costfunc())
        j1,j2 = ()
        self.t1 = self.t1 - n * j1
        self.t2 = self.t2 - n * j2
        t1s.append(self.t1)
        t2s.append(self.t2)

    print(self.t1,self.t2)
    return costs,t1s,t2s
