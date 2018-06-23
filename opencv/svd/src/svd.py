#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

def main():
    print("Main")
    A=np.array([[1,2,3],[4,5,6]])
    M,N=A.shape
    U,s,Vh=linalg.svd(A)
    Sig=linalg.diagsvd(s,M,N)
    U,Vh=U,Vh
    print("A: ",A)
    print("U: ",U)
    print("Sig: ",Sig)
    print("Vh: ",Vh)
    print("U.dot(Sig.dot(Vh))",U.dot(Sig.dot(Vh)))

if __name__ == "__main__":
    main()

