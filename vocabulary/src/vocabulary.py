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
    parser = argparse.ArgumentParser(description='Get smarter')
    parser.add_argument('words', type=int, default=0, nargs="?", help='max number of words to review, defalut "All"')

    args = parser.parse_args()
    return args.words

def main():

    words=[]
    words=readFile(words)
    p=parse()
    w = p if p != 0  else len(words)
    w = w if w < len(words) else len(words)
    deck = list(range(len(words)))
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)

    k=1
    for n in deck[:w]:
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + " (" + words['Type'][n] + ")\n\n\n\n\n\n\n\n\n\n\n")
        s=raw_input("Press Enter to continue ...")
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + " (" + words['Type'][n] + ")\n\n")
        print("\t\t\t\t\t\t\t\tDefinition: " + words['Definition'][n])
        print("\t\t\t\t\t\t\t\tSynonyms: " + words['Synonyms'][n])
        print("\t\t\t\t\t\t\t\tSentence: " + words['Sentence'][n])
        print("\t\t\t\t\t\t\t\tType: " + words['Type'][n])
        print("\t\t\t\t\t\t\t\tPronunciation: " + words['Pronunciation'][n])
        print("\t\t\t\t\t\t\t\tCount: " + str(k) + " of " + str(w) + "\n\n\n\n")
        k=k+1
        s=raw_input("Press Enter to continue ...")
        os.system('clear')
    print("\n\n\n\n\t\t\t\t\t\t\t\tAll Done(" + str(w) + "/" + str(w) +")!\n\n\n\n")

   

if __name__ == "__main__":
    main()

