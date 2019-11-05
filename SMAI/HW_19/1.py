#!/usr/bin/env python
# coding: utf-8

# In[57]:


import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
import numpy as np

def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    num_points = len(lines)
    dim_points = 28 * 28
    data = []
    labels = []
    
    for ind, line in enumerate(lines):
        num = line.split(',')
        if(int(num[0])<2):
            labels.append(int(num[0])) 
            data.append([ int(x) for x in num[1:] ])
        
    return (np.array(data), np.array(labels))

train_data, train_labels = read_data("sample_train.csv")
test_data, test_labels = read_data("sample_test.csv")

print(train_data.shape, test_data.shape)
print(train_labels.shape, test_labels.shape)


# In[75]:


# new class
class MLPClassifierOverride(MLPClassifier):

    def _init_coef(self, fan_in, fan_out):
        if self.activation == 'logistic':
            init_bound = np.sqrt(2. / (fan_in + fan_out))
        elif self.activation in ('identity', 'tanh', 'relu'):
            init_bound = np.sqrt(6. / (fan_in + fan_out))
        else:
            raise ValueError("Unknown activation function %s" %
                             self.activation)
        coef_init = np.random.random((fan_in, fan_out)) # change it to np.zeros or np.ones for 0 and 1 respectively

        intercept_init = np.random.random(fan_out)

        return coef_init, intercept_init


# In[76]:


clf = MLPClassifierOverride(alpha = 1e-5,hidden_layer_sizes=(784,784),max_iter=100,verbose=True)


# In[77]:


clf.fit(train_data,train_labels)


# In[81]:


predicted = clf.predict(test_data)
accuracy = 0
for i in range(len(test_data)):
    if(predicted[i]==test_labels[i]):
        accuracy+=1
print(accuracy/2)


# In[ ]:





# In[ ]:




