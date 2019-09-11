import numpy as np
import pickle
from matplotlib import pyplot as plt

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

data1 = unpickle('cifar-10-batches-py/data_batch_1')
data2 = unpickle('cifar-10-batches-py/data_batch_2')
data3 = unpickle('cifar-10-batches-py/data_batch_3')
data4 = unpickle('cifar-10-batches-py/data_batch_4')
data5 = unpickle('cifar-10-batches-py/data_batch_5')
data = np.vstack((data1[b'data'],data2[b'data'],data3[b'data'],data4[b'data'],data5[b'data']))
labels = np.vstack((data1[b'labels'],data2[b'labels'],data3[b'labels'],data4[b'labels'],data5[b'labels']))
labels = labels.flatten()

if __name__ == "__main__":
    values,vectors = np.linalg.eig(np.cov(data.T))
    
    indices = np.argsort(labels)
    data = data[indices]
    labels = labels[indices]
    
    indices = np.argsort(values)
    vectors = vectors[indices]
    values = values[indices]

    fig1 = plt.figure()
    p1 = fig1.add_subplot(111,title="Eigen Values")
    p1.plot(values)

    plt.show()
