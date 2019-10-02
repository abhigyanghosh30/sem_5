import numpy as np
data = [[1, 1, 1],
    [-1, -1, 1 ],
    [ 2, 2, 1],
    [-2, -2, 1],
    [-1, 1, 1], 
    [1 ,1, 1]]
labels = np.array([-1,-1,1,-1,1,1])

its = 0

def batch_perp(w,n=0.4):

    print(w)

    global its
    its += 1
    if(its>100):
        return [0,0,0]

    errors = []
    
    for i in range(len(data)):
        clas = np.matmul(w.T,data[i])
        if(clas*labels[i]<0):
            errors.append((data[i],labels[i]))

    if len(errors) == 0:
        return w

    else:
        w_1=[w[0],w[1],w[2]]
        for i in range(len(errors)):
            w_1[0] += errors[i][0][0] * 2 * n * errors[i][1]
            w_1[1] += errors[i][0][1] * 2 * n * errors[i][1]
            w_1[2] += errors[i][0][2] * 2 * n * errors[i][1]

        return batch_perp(np.array(w_1))    



print(batch_perp(np.array([1,0,0])))