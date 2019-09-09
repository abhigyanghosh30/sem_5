import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

x = np.array([i for i in range(-500,500)])
x=x/100
y = np.array([2*i+3 for i in x])
error = np.random.normal(0,1,1000)
y = y + error

fig1 = plt.figure()
p1 = fig1.add_subplot(111,title='Data Points')
p1.scatter(x,y,s=0.2)


class GD:

    def __init__(self):
        self.t1 = 0
        self.t2 = 0 

    def cost_MSE(self):
        cost = 0
        for i in range(1000):
            cost += np.square(self.t1 * x[i] + self.t2 - y[i])
        return cost/2000
    
    def cost_MAE(self):
        cost = 0
        for i in range(1000):
            cost += np.absolute(self.t1 * x[i] + self.t2 - y[i])
        return cost/1000

    def cost_LCE(self):
        cost = 0
        for j in range(1000):
            cost += np.log(np.cosh(self.t1 * x[j] + self.t2 - y[j]))
        return cost

    def dev_MSE(self):
        s1 = s2 = 0
        for j in range(1000):
            s1 += x[j]*(self.t1 * x[j] + self.t2 - y[j])
            s2 += (self.t1 * x[j] + self.t2 - y[j])
        return s1/1000,s2/1000

    def dev_MAE(self):
        s1 = s2 = 0
        for j in range(1000):
            if (self.t1 * x[j] + self.t2 - y[j])>0 :
                s1 += x[j]
                s2 += 1
            else :
                s1 -= x[j]
                s2 -= 1
        return s1/1000,s2/1000

    def dev_LCE(self):
        s1 = s2 = 0
        for j in range(1000):
            s1 += x[j]*np.sinh(self.t1 * x[j] + self.t2 - y[j])/np.cosh(self.t1 * x[j] + self.t2 - y[j])
            s2 += np.sinh(self.t1 * x[j] + self.t2 - y[j])/np.cosh(self.t1 * x[j] + self.t2 - y[j])
        return s1,s2

    def gradient_descent(self,costfunc,devfunc,n=0.01,iterations=1000):
        costs = []
        t1s = []
        t2s = []
        for i in range(iterations):
            costs.append(costfunc())
            j1,j2 = devfunc()
            self.t1 = self.t1 - n * j1
            self.t2 = self.t2 - n * j2
            t1s.append(self.t1)
            t2s.append(self.t2)

        print(self.t1,self.t2)
        return costs,t1s,t2s

def cost_MSE1(t1,t2):
    cost = 0
    for i in range(len(x)):
        cost += np.square(t1 * x[i] + t2 - y[i])
    return cost/2000

def cost_MAE1(t1,t2):
    cost = 0
    for i in range(len(x)):
        cost += np.absolute(t1 * x[i] + t2 - y[i])
    return cost/1000

def cost_LCE1(t1,t2):
    cost = 0
    for j in range(len(x)):
        cost += np.log(np.cosh(t1 * x[j] + t2 - y[j]))
    return cost

if __name__ == "__main__":
    fig2 = plt.figure()

    p21 = fig2.add_subplot(131,title = 'Mean Square Error',xlabel = 'iteration',ylabel='Cost')
    MSEobj = GD()
    MSEcosts,MSEt1s,MSEt2s = MSEobj.gradient_descent(MSEobj.cost_MSE,MSEobj.dev_MSE)
    p21.plot(MSEcosts)

    p22 = fig2.add_subplot(132,title = 'Mean Absolute Error',xlabel = 'iteration',ylabel='Cost')
    MAEobj = GD()
    MAEcosts,MAEt1s,MAEt2s = MAEobj.gradient_descent(MAEobj.cost_MAE,MAEobj.dev_MAE)
    p22.plot(MAEcosts)
    
    p23 = fig2.add_subplot(133,title = 'log cosh Error',xlabel = 'iteration',ylabel='Cost')
    LCEobj = GD()
    LCEcosts,LCEt1s,LCEt2s = LCEobj.gradient_descent(LCEobj.cost_LCE,LCEobj.dev_LCE,n=0.0001)
    p23.plot(LCEcosts)
    
    fig3 = plt.figure()
    xsp = np.linspace(-100,100,100)
    ysp = np.linspace(-100,100,100)
    X, Y = np.meshgrid(xsp, ysp)

    ax = fig3.add_subplot(131,projection='3d')
    Z = cost_MSE1(X,Y)    
    ax.view_init(10,45)
    ax.set_xlabel('theta1')
    ax.set_ylabel('theta2')
    ax.set_zlabel('loss')
    ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    ax = fig3.add_subplot(132,projection='3d')
    Z = cost_MAE1(X,Y)
    ax.view_init(10,45)
    ax.set_xlabel('theta1')
    ax.set_ylabel('theta2')
    ax.set_zlabel('loss')

    ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    ax = fig3.add_subplot(133,projection='3d')
    Z = cost_LCE1(X,Y)
    ax.view_init(10,45)
    ax.set_xlabel('theta1')
    ax.set_ylabel('theta2')
    ax.set_zlabel('loss')
    ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.show()