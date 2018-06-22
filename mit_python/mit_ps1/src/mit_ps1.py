#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

def main():
    annual_salary=float(input("Enter your annual salary: "))
    #annual_salary=130000
    portion_saved=float(input("Enter your portion of annual salary to be saved: "))*annual_salary
    print("Portion Saved: " + str(portion_saved))
    #portion_saved=annual_salary*.1
    total_cost=float(input("Enter the cost of your dream home: "))
    #total_cost=377000
    portion_down_payment=total_cost*0.25
    current_savings=0
    r=0.04

    months=0
    while current_savings < portion_down_payment :
        current_savings+=(portion_saved + current_savings*r)/12.0
        months+=1
    print("It will take you " + str(months) + " months to save a down payment of " + str(portion_down_payment))




    

if __name__ == "__main__":
    main()

