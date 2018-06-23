#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

def main():
    print("Main")
    A=np.array([[1,2],[3,4]])
    b=np.array([[5],[6]])

    print("A: ",A)
    print("b: ",b)
    print("A^-1*b: ",linalg.inv(A).dot(b))
    print("A^-1*b - b: ",A.dot(linalg.inv(A).dot(b))-b)
    print("Solve(A,b): ",np.linalg.solve(A,b))
    print("Solve(A,b) - b: ",A.dot(np.linalg.solve(A,b))-b)

if __name__ == "__main__":
    main()

