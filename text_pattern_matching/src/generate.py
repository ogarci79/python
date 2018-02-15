#!/usr/bin/env python

import sys, time, argparse
import random
import string

def main():
    parser = argparse.ArgumentParser(description='Match a pattern')
    parser.add_argument('-n','--numChars',default=1000,help='Number of chars to create',required=False)
    parser.add_argument('-o','--outFile',default='output.txt',help='Name of output file',required=False)
    args=vars(parser.parse_args())

    numChars=args['numChars']
    outFile=args['outFile']

    file=open(outFile,"wp")
    for ch in range(int(numChars)) :
        file.write(random.choice(string.ascii_letters))
    file.write("\n")
    file.close()

if __name__ == "__main__":
    main()

