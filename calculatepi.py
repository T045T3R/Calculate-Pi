"""
calculatepi.py
Author: Johannes Testorf
Credit: Wilson Wrimberg
Assignment:

Write and submit a Python program that computes an approximate value of π by calculating the following sum:

(see: https://github.com/HHS-IntroProgramming/Calculate-Pi/blob/master/README.md)

This sum approaches the true value of π as n approaches ∞.

Your program must ask the user how many terms to use in the estimate of π, how many decimal places, 
then print the estimate using that many decimal places. Exactly like this:

I will estimate pi. How many terms should I use? 100
How many decimal places should I use in the result? 7
The approximate value of pi is 3.1315929


Note: remember that the printed value of pi will be an estimate!

"""
n = input ("I will estimate pi. How many terms should I use? ")
decimals=input ("How many decimal places should I use in the result? ")
intlist = range(0, int(n))
pi = lambda n: (4*((-1)**n)/((2*n)+1))
pidigits = [pi(x) for x in list(intlist)]
PI = sum(pidigits)
print("The approximate value of pi is ".format(round(PI, decimals)))
