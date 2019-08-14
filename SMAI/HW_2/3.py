import sys
import random
import json
import numpy as np
import matplotlib
from matplotlib import pyplot as plt 
matplotlib.use('TKagg')

input = np.array([1,1,0.3])


ax = []
bx = []
ay = []
by = [] 

with open('data.json', 'r') as f:
    scatter = json.load(f)
#     print(scatter)
    ax = scatter["ax"]
    ay = scatter["ay"]
    bx = scatter["bx"]
    by = scatter["by"]




def generate():

    ax = []
    ay = []
    bx = []
    by = []
    for i in range(0,50):
        ax.append(random.uniform(-1,1))
        bx.append(random.uniform(-1,1))
        ay.append(random.uniform(-1,1))
        by.append(random.uniform(-1,1))

        with open('data.json','w') as f:
                data = {
                        "ax": ax,
                        "ay": ay,
                        "bx": bx,
                        "by": by
                }
                json.dump(data,f)

def calculate():
    accuracy = 0
    for i in range(0,50):
        wtx = np.dot(input,np.array([ax[i],ay[i],1]))
        print(ax[i],ay[i],wtx)
        if(wtx>0):
            accuracy+=1


    for i in range(0,50):
        wtx = np.dot(input,np.array([bx[i],by[i],1]))
        print(bx[i],by[i],wtx)
        if(wtx<0):
            accuracy+=1

    print(accuracy)


def plot():
    plt.scatter(ax,ay,marker='o')
    plt.scatter(bx,by,marker='x')
    x = np.linspace(-1, 1, 100)
    plt.plot(x, -x, linestyle='--', color='blue')
    # plt.plot(x, -x, linestyle='--', color='green')
    # plt.plot(x-x, -x, linestyle='--', color='yellow')
    plt.plot(x, x+5, linestyle='--', color='green')
    plt.plot(x,-x-0.3, linestyle='--', color='red')
    plt.show()

def main():
    # generate()
    # calculate()
    plot()

if __name__ == '__main__' : 

    main()

 
