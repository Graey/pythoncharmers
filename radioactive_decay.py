# calculate evolved time

import math

print("enter the initial number of nucleases")
no=float(input())
print("enter the present number of nucleases")
n=float(input())
print("enter the activity")
a=float(input())

time_evolved=(math.log(no/n))/a

print("time evolved: ",time_evolved)
