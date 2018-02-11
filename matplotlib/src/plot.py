#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

def plot(x,y):
    plt.plot(x,y,'r',label='Random Stuff')
    plt.ylabel('Random Values',fontsize=24)
    plt.xlabel('Index',fontsize=24)
    plt.title('Junk',fontsize=30)
    plt.legend()
    plt.show(block=False)


def getRand():
    np.random.seed(0)
    return np.random.randint(10,size=(1,10))

def getMatrix(a,b):
    np.random.seed(0)
    return np.random.randint(10,size=(a,b))
    
def main():
    y=getRand()
    x=range(y.size)

    M=getMatrix(2,2)
    N=getMatrix(2,1)
    print("M:",M)
    print("N:",N)
    print("M*N:",np.matmul(M,N))
    print("M*N:",M.dot(N))
    print("M^-1:",linalg.inv(M))
    print("M*M^-1:",M.dot(linalg.inv(M)))

    #plot(x,y)
    #plt.show()

if __name__ == "__main__":
    main()

