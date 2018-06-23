#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

def main():
    print("Main")
    A=np.mat('[1 3 2;1 4 5;2 3 6]')
    T,Z=linalg.schur(A)
    T1,Z1=linalg.schur(A,'complex')
    T2,Z2=linalg.rsf2csf(T,Z)
    print("A: ",A)
    print("abs(T1-T2): ",abs(T1-T2))
    print("abs(Z1-Z2): ",abs(Z1-Z2))
    T,Z,T1,Z1,T2,Z2=map(np.mat,(T,Z,T1,Z1,T2,Z2))
    print("abs(A-Z*T*Z.H): ",abs(A-Z*T*Z.H))
    print("abs(A-Z1*T1*Z1.H): ",abs(A-Z1*T1*Z1.H))
    print("abs(A-Z2*T2*Z2.H): ",abs(A-Z2*T2*Z2.H))

if __name__ == "__main__":
    main()

