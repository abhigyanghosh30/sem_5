import numpy as np 
from matplotlib import pyplot as plt 
from sklearn.model_selection import KFold
import os


x_100 = np.array([ i for i in range(100)])
x_10000 = np.array([ i for i in range(10000)])


def generate():

    n_100 = np.random.normal(0,1,100)
    n_10000 = np.random.normal(0,1,10000)

    np.save('data_1_n1000.npy',n_10000)
    np.save('data_1_n100.npy',n_100)

def calculate():

    # if os.path.isfile('data_1_n100.npy'):
    n_100 = np.load('data_1_n100.npy')

    # if os.path.isfile('data_1_n1000.npy'):
    n_10000 = np.load('data_1_n1000.npy')



    y_100 = np.sin(x_100) + n_100
    y_10000 = np.sin(x_10000) + n_10000

    folds = [2,5,10,20,25,50]
    
    mean_var_100 = []

    for fold in folds:
        kf = KFold(fold,True,1)

        fold_means = []

        for train, test in kf.split(x_100):
            sample_errs = [n_100[i] for i in x_100[train]]
            fold_means.append(np.mean(np.array(sample_errs)))
        mean = np.mean(fold_means)
        var = np.var(fold_means)
        mean_var_100.append((fold, mean, var))    

    folds = []
    for i in range(2, 10000):
        if(10000 % i == 0):
            folds.append(i)

    mean_var_10000 = []

    for fold_num in folds:
        kfold = KFold(fold_num, True, 1)

        fold_means = []

        for train, test in kfold.split(x_10000):
            #print("Train: ", (data_100[train]), " Test: ", (data_100[test]))
            sample_errs = [n_10000[i] for i in x_10000[train]]
            fold_means.append(np.mean(np.array(sample_errs)))

        #print(fold_means)
        mean = np.mean(fold_means)
        var = np.var(fold_means)
        mean_var_10000.append((fold_num, mean, var))

    print(mean_var_10000)

    x = [a[0] for a in mean_var_100]
    y_dev = [a[2] for a in mean_var_100]
    y_mean = [a[1] for a in mean_var_100]

    x_b = [a[0] for a in mean_var_10000]
    y_b_dev = [a[2] for a in mean_var_10000]
    y_b_mean = [a[1] for a in mean_var_10000]

    fig = plt.figure()

    p_1 = fig.add_subplot(221, title='100 Points: Error Variance v/s K')
    p_1.plot(x, y_dev, 'o', linestyle = '-', color = 'k')
    p_2 = fig.add_subplot(222, title='100 Points: Error Mean v/s K')
    p_2.plot(x, y_mean,'o', linestyle = '-', color = 'k')


    p_3 = fig.add_subplot(223, title='10000 Points: Error Variance v/s K')
    p_3.plot(x_b, y_b_dev, 'o', linestyle = '-', color = 'k')
    p_4 = fig.add_subplot(224, title='10000 Points: Error Mean v/s K')
    p_4.plot(x_b, y_b_mean,'o', linestyle = '-', color = 'k')

    plt.show()

if __name__ == "__main__":
    # generate()
    calculate()