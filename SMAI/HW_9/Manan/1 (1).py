import numpy as np
import matplotlib.pyplot as plt


X = 2 * np.random.rand(1000,1)
y = 1 + 2 * X + np.random.normal(0, 0.1, (1000, 1))

plt.scatter(X, y, s=[0.1])
plt.show()

def  cal_cost(theta,X,y):
    
    m = len(y)
    
    predictions = X.dot(theta)
    cost = (1/2*m) * np.sum(np.square(predictions-y))
    return cost


def gradient_descent(X,y,theta,learning_rate=0.01,iterations=100):
    m = len(y)
    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations,2))
    for it in range(iterations):
        
        prediction = np.dot(X,theta)
        
        theta = theta -(1/m)*learning_rate*( X.T.dot((prediction - y)))
        theta_history[it,:] =theta.T
        cost_history[it]  = cal_cost(theta,X,y)
        
    return theta, cost_history, theta_history

lr =0.01
n_iter = 1000

theta = np.random.randn(2,1)

X_b = np.c_[np.ones((len(X),1)),X]
theta,cost_history,theta_history = gradient_descent(X_b,y,theta,lr,n_iter)

plt.plot(np.arange(1000), cost_history)

print('Theta0:          {:0.3f},\nTheta1:          {:0.3f}'.format(theta[0][0],theta[1][0]))
print('Final cost/MSE:  {:0.3f}'.format(cost_history[-1]))
plt.show()


def cal_MAE(theta,X,y):
    m = len(y)
    
    predictions = X.dot(theta)
    cost = (1/m) * np.sum(np.absolute(predictions-y))
    return cost


def gradient_descent_MAE(X,y,theta,learning_rate=0.01,iterations=100):
    m = len(y)
    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations,2))
    for it in range(iterations):
        
        prediction = np.dot(X,theta)
        grad1 = 0
        grad2 = 0
        for i in range(len(X)):
            grad1 += X[i][1] * (np.dot(theta[:, 0], X[i]) - y[i]) / np.absolute((np.dot(theta[:, 0], X[i]) - y[i]))
        for i in range(len(X)):
            grad2 += (np.dot(theta[:, 0], X[i]) - y[i]) / np.absolute((np.dot(theta[:, 0], X[i]) - y[i]))
        theta[0] = theta[0] - learning_rate * grad2 * 1/m
        theta[1] = theta[1] - learning_rate * grad1 * 1/m
        
        
        theta_history[it,:] =theta.T
        cost_history[it]  = cal_MAE(theta,X,y)
        
    return theta, cost_history, theta_history

lr =0.01
n_iter = 1000

theta = np.random.randn(2,1)

X_b = np.c_[np.ones((len(X),1)),X]
theta,cost_history,theta_history = gradient_descent_MAE(X_b,y,theta,lr,n_iter)

plt.plot(np.arange(1000), cost_history)

print('Theta0:          {:0.3f},\nTheta1:          {:0.3f}'.format(theta[0][0],theta[1][0]))
print('Final cost/MAE:  {:0.3f}'.format(cost_history[-1]))
plt.show()

def cal_logcosh(theta,X,y):
    m = len(y)
    
    predictions = X.dot(theta)
    cost = (1/m) * np.sum(np.log(np.cosh(predictions-y)))
    return cost


def gradient_descent_logcosh(X,y,theta,learning_rate=0.01,iterations=100):
    m = len(y)
    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations,2))
    for it in range(iterations):
        
        prediction = np.dot(X,theta)
        grad1 = 0
        grad2 = 0
        for i in range(len(X)):
            grad1 += X[i][1] * np.sinh(np.dot(theta[:, 0], X[i]) - y[i]) / np.cosh(np.dot(theta[:, 0], X[i]) - y[i])
        for i in range(len(X)):
            grad2 += np.sinh(np.dot(theta[:, 0], X[i]) - y[i]) / np.cosh((np.dot(theta[:, 0], X[i]) - y[i]))
        theta[0] = theta[0] - learning_rate * grad2 * 1/m
        theta[1] = theta[1] - learning_rate * grad1 * 1/m
        
        
        theta_history[it,:] =theta.T
        cost_history[it]  = cal_logcosh(theta,X,y)
        
    return theta, cost_history, theta_history


# In[352]:


lr =0.01
n_iter = 1000

theta = np.random.randn(2,1)

X_b = np.c_[np.ones((len(X),1)),X]
theta,cost_history,theta_history = gradient_descent_logcosh(X_b,y,theta,lr,n_iter)

plt.plot(np.arange(1000), cost_history)
plt.show()
print('Theta0:          {:0.3f},\nTheta1:          {:0.3f}'.format(theta[0][0],theta[1][0]))
print('Final cost/LogCosh:  {:0.3f}'.format(cost_history[-1]))


# In[ ]:




