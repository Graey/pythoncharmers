# Python3 Program to find sum of square of first n natural numbers 

 

# Return the sum of square of first n natural numbers 
def squaresum(n) : 

	# Iterate i from 1 and n finding square of i and add to sum. 
	sum = 0
	for i in range(1, n+1) : 
		sum = sum + (i * i) 
	
	return sum 


n = int(input("Upto which number:"))
print(squaresum(n)) 



