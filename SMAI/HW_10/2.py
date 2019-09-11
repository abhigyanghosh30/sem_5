import csv
import numpy as np
from matplotlib import pyplot as plt


data_rows=[]
data_labels=[]
with open('wine.data','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        data_rows.append(row[1:])
        data_labels.append(row[0])
data_rows = np.matrix(data_rows).astype(np.float) 

cov = np.cov(data_rows.T)
print(cov.shape)
values,vectors = np.linalg.eig(cov)
index = np.argsort(values)
values = values[index]
vectors = vectors[index]

fig1 = plt.figure()
p1 = fig1.add_subplot(111,title='Eigenvalues Plot')
p1.plot(values)

red_data = np.dot(vectors[:2],data_rows.T)
red_data = np.matrix(red_data)


fig2 = plt.figure()
p2 = fig2.add_subplot(111,title='Scatter')
p2.scatter(np.array(red_data[0,:60]),np.array(red_data[1,:60]),c='r')
p2.scatter(np.array(red_data[0,60:130]),np.array(red_data[1,60:130]),c='g')

plt.show()