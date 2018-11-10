#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import argparse
import csv
import os
import pandas as pd
import random
from scipy import linalg 

def readFile(words):
    words=pd.read_csv('words.csv')
    return words


def parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)

def main():

    words=[]
    words=readFile(words)
    deck = list(range(len(words)))
    random.shuffle(deck)

    k=1
    for n in deck:
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + "\n\n\n\n\n\n\n\n\n\n\n")
        s=raw_input("Press Enter to continue ...")
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + "\n\n")
        print("\t\t\t\t\t\t\t\tDefinition: " + words['Definition'][n])
        print("\t\t\t\t\t\t\t\tSynonyms: " + words['Synonyms'][n])
        print("\t\t\t\t\t\t\t\tSentence: " + words['Sentence'][n])
        print("\t\t\t\t\t\t\t\tType: " + words['Type'][n])
        print("\t\t\t\t\t\t\t\tPronunciation: " + words['Pronunciation'][n])
        print("\t\t\t\t\t\t\t\tCount: " + str(k) + "\n\n\n\n")
        k=k+1
        s=raw_input("Press Enter to continue ...")
        os.system('clear')
   

if __name__ == "__main__":
    main()

