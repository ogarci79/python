#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

def main():
    print("Main")
    A=np.array([[1,2],[3,4]])
    print("A: ",A)
    print("det(A): ",linalg.det(A))

if __name__ == "__main__":
    main()

