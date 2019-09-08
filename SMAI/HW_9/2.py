import numpy as np

def gradient_descent(x,n=0.1,iterations=1000):
    for i in range(iterations):
        x -= n * 2 * x  # dy/dx of x^2 is 2x
    return x, x*x

if __name__ == "__main__":
    print(gradient_descent(x=-2))