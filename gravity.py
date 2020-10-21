# calculate gravitational force

import math

print("enter the mass of the first body in kg")
m1=float(input())
print("enter the mass of the second body in kg")
m2=float(input())
print("enter the distance between them in m")
d=float(input())

force=(6.67*math.pow(10,-11)*m1*m2/(d*d))

print("Force=",force,"N")
