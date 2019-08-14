import json
import numpy as np

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