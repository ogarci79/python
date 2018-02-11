#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg 

def main():
    print("Main")
    A=np.array([[1,2],[3,4]])
    la,v=linalg.eig(A)
    l1,l2=la
    print("Eigenvalues: ",l1,l2)
    print("Eigenvector: ",v[:,0])
    print("Eigenvector: ",v[:,1])
    print(np.sum(abs(v**2),axis=0))
    v1=np.array(v[:,0]).T
    print(linalg.norm(A.dot(v1)-l1*v1))

if __name__ == "__main__":
    main()

