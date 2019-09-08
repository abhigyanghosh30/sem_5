import numpy as np
from matplotlib import pyplot as plt

vars = []

for x in range(200,100000,200):
    data = np.random.normal(0,1,x)
    sets = np.split(data,200)
    mle = []
    for i in range(200):
        mle.append(np.mean(sets[i]))
    vars.append(np.var(mle))

fig = plt.figure()
p1 = fig.add_subplot(121,title='K vs variance | s = 200',xlabel='k',ylabel='variance')
p1.scatter([i for i in range(0,len(vars))],vars)
# p1.xlabel('k')
# p1.ylabel('variance')

vars = []
for x in range(1,201):
    # k = 500
    data = np.random.normal(0,1,500*x)
    sets = np.split(data,x)
    mle = []
    for i in range(x):
        mle.append(np.mean(sets[i]))
    vars.append(np.var(mle))

p2 = fig.add_subplot(122,title='s vs variance | k = 500',xlabel='s',ylabel='variance')
p2.scatter([i for i in range(0,len(vars))],vars)

plt.show()
