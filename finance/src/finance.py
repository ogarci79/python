#!/usr/bin/env python

#import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
from scipy import optimize 
#from scipy import linalg 

def H(r,m):
    return np.power(r+1,m)

def L(r,m):
    return np.power(r+1,m-1)

def I(r,m,c):
    return c*r*L(r,m)

def J(r,m,c):
    return c*L(r,m)

def K(r,m):
    return (H(r,m) - 1) / r

def T(r,m,c):
    return c*H(r,m)

def solvePayment(r,m,c,f):
    print ('Payment: ${0:1.2f}' % (f-I(r,m,c)-J(r,m,c))/K(r,m))

def solveFuture(p,r,m,c):
    print ('Future Value: ${0:1.2f}' % I(r,m,c)+J(r,m,c)+p*K(r,m))

def solveCurrent(p,r,m,f):
    print ('Current Value: ${0:1.2f}' % (f-p*K(r,m))/H(r,m))

def func1(x,p,r,f,c):
    return c*np.power(r+1,x) + p*(np.power(r+1,x)-1)/r - f

def func2(x,p,m,f,c):
    return c*np.power(x+1,m) + p*(np.power(x+1,m)-1)/x - f

def solveMonths(p,r,f,c):
    print ("Hi")
    print ('Months: %1.2f' % optimize.newton(func1,10,fprime=None,args=(p,r,f,c)))

def solveRate(p,m,f,c):
    print ('Rate: {0:1.4f}' % 12*optimize.newton(func2,0.01,fprime=None,args=(p,m,f,c)))

def amortization(p,r,f,c):
    file=open('amortization.txt',"w")
    file.write("Month,Beginning Balance,Payment,Principle,Interest,End Balance\n")

    n=1
    x=c
    x_last=c
    eps=np.fabs(x-f)
    while eps > np.fabs(p/2):
        interest=x_last*r
        principle=p+interest
        x=x_last + interest + p
        file.write("{0:1.0f},${1:1.2f},${2:1.2f},${3:1.2f},${4:1.2f},${5:1.2f}\n".format(n,x_last,p,principle,interest,x))
        x_last=x
        n=n+1
        eps=np.fabs(x-f)

    file.close() 



    

def main():
    parser = argparse.ArgumentParser(description='Solve Financial Math')
    parser.add_argument('-p','--payment',help='Monthly Payment',required=False,type=float)
    parser.add_argument('-r','--rate',help='Annual Percentage Rate',required=False,type=float)
    parser.add_argument('-m','--months',help='Number of Months',required=False,type=float)
    parser.add_argument('-e','--evaluate',help='Evaluate at month',required=False,type=float)
    parser.add_argument('-c','--currentValue',help='Current Value',required=False,type=float)
    parser.add_argument('-f','--futureValue',help='Future Value',required=False,type=float)
    args=vars(parser.parse_args())

    p=args['payment']
    if args['rate'] is None:
        r=None
    else:
        r=(args['rate']/12)
    m=args['months']
    e=args['months']
    c=args['currentValue']
    f=args['futureValue']

    if (len(sys.argv) < 9): 
        print ("Insufficient Number of Arguments. Need four of (p-payment,r-rate,m-months,e-not_used,c-currentValue,f-futureValue)")
        exit(-1)

    if p is None:
        solvePayment(r,m,c,f)
        exit(-1)

    if f is None:
        solveFuture(p,r,m,c)
        exit(-1)

    if c is None:
        solveCurrent(p,r,m,f)
        exit(-1)

    if r is None:
        solveRate(p,m,f,c)
        exit(-1)

    amortization(p,r,f,c)

    if m is None:
        solveMonths(p,r,f,c)
        exit(-1)



if __name__ == "__main__":
    main()

