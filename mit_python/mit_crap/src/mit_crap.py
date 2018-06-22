#!/usr/bin/env python

#import matplotlib.pyplot as plt
#import numpy as np
#from scipy import linalg 

def main():
    #x = float(input("Enter a number for x: "))
    #y = float(input("Enter a number for y: "))
    #if x == y:
    #    print("x and y are equal")
    #    if y != 0:
    #        print("therefore, x / y is", x/y)
    #elif x < y:
    #        print("x is smaller")
    #else:
    #        print("y is smaller")
    #print("thanks!")
    #s="abcdefghijklmnopqrstuvwxyz"

    #for char in s:
    #    if char == 'i':
    #        print("Has i")

    cube = 1000
    cube = 8120601
    cube = 10000
    epsilon = 0.1
    guess = 0.0
    increment = 0.01
    num_guesses = 0
    while abs(guess**3 - cube) >= epsilon and guess**3 < cube:
        guess += increment
        num_guesses += 1
    print('num_guesses =', num_guesses)
    if abs(guess**3 - cube) >= epsilon:
        print('Failed on cube root of', cube)
    else:
        print(guess, 'is close to the cube root of', cube)


if __name__ == "__main__":
    main()

