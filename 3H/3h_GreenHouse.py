import math 
import sys


x = input("What is the Rating of the seeds? ")
x = int(x)
g = input("what is the grade of the seeds? ")
g = int(g)
n = input("how many seeds? ")
n = int(n)

y = x*n
z = g*n

tot = y % 12
gtot = z/5

A = (12 - tot) * 5
B = math.floor(gtot*4)
C = 20

Value = A + B + C
print(Value)
stuff = .7*.2
stuff = stuff*14
print(stuff)