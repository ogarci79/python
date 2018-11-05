#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import argparse
import csv
import random
from scipy import linalg 

def readFile(words):
    with open('words.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print row['Word']


def parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)

def main():
    words=[]
    #print("Main")
    readFile(words)
    #parse()
    #n=random.randint(0,len(words[0])-1)
    #print words['Word'][n]
   

if __name__ == "__main__":
    main()

