# Python3 Program to
# find sum of square
# of first n natural 
# numbers
  
  
# Return the sum of
# square of first n
# natural numbers
def squaresum(n) :
  
    # Iterate i from 1 
    # and n finding 
    # square of i and
    # add to sum.
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
      
    return sm
  
# Driven Program
n = 4
print(squaresum(n))
