# calculate gravitational force

import math

print("enter the charge of the first body in C")
q1=float(input())
print("enter the charge of the second body in C")
q2=float(input())
print("enter the distance between them in m")
d=float(input())

force=(9*math.pow(10,9)*q1*q2/(d*d))

print("Force=",force,"N")
