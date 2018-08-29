#Objective In this challenge, you'll work with arithmetic operators.
#Task Given the m e al p ric e (base cost of a meal), tip p e r c e n t (the percentage of the m e al p ric e being added as tip),
#and t a x p e r c e n t (the percentage of the m e al p ric e being added as tax) for a meal, 
#find and print the meal's t o t al c o s t . Note: Be sure to use precise values for your calculations,
#or you may end up with an incorrectly rounded result! Input Format There are  lines of numeric input: The first line has a double, 
#(the cost of the meal before tax and tip). The second line has an integer,  (the percentage of  being added as tip).
#The third line has an integer,  (the percentage of  being added as tax).
#Output Format Print The total meal cost is totalCost dollars., 
#where  is the rounded integer result of the entire bill ( with added tax and tip).
#Sample Input
#12.00 20 8
#Sample Output
#The total meal cost is 15 dollars.

#Explanation
#given:
#mealCost=12, tipPercent = 20, taxPercent = 8
#Calculation:
#tip=(12*20)/100
#tax=(12*8)/100
#total cost = mealcost+tip+tax=15.36
#round(tota cost)=15

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    __name__='__main__'
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = (int(input())*meal_cost)/100
    
    tax_percent = (int(input())*meal_cost)/100
    total=(meal_cost+tip_percent+tax_percent)
print ("The total meal cost is" , round(total), "dollars.")
solve(meal_cost, tip_percent, tax_percent)