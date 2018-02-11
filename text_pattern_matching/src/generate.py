#!/usr/bin/env python

import sys, time
import random
import string

def main():
    numChars=sys.argv[1]

    file=open("input.txt","wp")
    for ch in range(int(numChars)) :
        file.write(random.choice(string.ascii_letters))
    file.write("\n")
    file.close()

if __name__ == "__main__":
    main()

