#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

def calc_savings(savings, monthly_savings, semi_annual_raise, r, total_months):
    months=0
    for months in range(total_months):
        if months % 6 == 1 and months > 1 :
            monthly_savings=monthly_savings*(1+semi_annual_raise)
        savings+=(monthly_savings + savings*r)
    return savings


def main():
    #monthly_savings=float(input("Enter your portion of annual salary to be saved: "))*annual_salary
    #total_cost=float(input("Enter the cost of your dream home: "))
    #semi_annual_raise=float(input("Enter your semi annual raise: "))

    #guess=0
    #hi=

    annual_salary=float(input("Enter your annual salary: "))

    total_cost=1.0e6
    r=0.04
    semi_annual_raise=.07
    savings=0

    down_payment = total_cost*0.25
    epsilon = 100
    num_guesses = 0
    low = 0 
    high = 10000
    guess = (high + low)/2.0
    #guess=2411
    dec_guess=float(guess)/high
    monthly_salary=annual_salary/12.0
    monthly_savings=dec_guess*float(monthly_salary)

    while abs(calc_savings(savings,monthly_savings,semi_annual_raise,r,36) - down_payment) >= epsilon and num_guesses < 1000:
        if calc_savings(savings,monthly_savings,semi_annual_raise,r,36) < down_payment :
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        dec_guess=float(guess)/10000
        monthly_savings=dec_guess*float(monthly_salary)
        num_guesses += 1
    print('num_guesses = ' + str(num_guesses))
    print("best rate: " + str(dec_guess) + " monthly_savings: " + str(monthly_savings) + " savings: " + str(calc_savings(savings,monthly_savings,semi_annual_raise,r,36)))




    

if __name__ == "__main__":
    main()

