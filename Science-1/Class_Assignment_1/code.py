import random
from matplotlib import pyplot as plt

def new_x(x):
    if(random.random()>0.5):
        return x+1
    else:
        return x-1

def player_movement(N):
    player_1 = 0
    player_2 = 0
    for i in range(N):
        player_1 = new_x(player_1)
        player_2 = new_x(player_2)
    if player_1 == player_2:
        return True
    else:
        return False

def simulation(n=10000):
    P = []
    for N in range(1,100):
        count = 0
        for i in range(n):
            if player_movement(N):
                count+=1
        P.append(count/n)
    plt.plot(P)
    plt.ylabel('P(N)')    
    plt.xlabel('N')
    plt.show()

if __name__ == "__main__":
    simulation()

