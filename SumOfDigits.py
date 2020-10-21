# Python3 Program to find the sum of digits of a number

def digitSum(n) :
	sumOfDigits = 0
	while (n ~= 0):
        digit = n % 10
        sumOfDigits = 10 * sumOfDigits + digit
        n /= 10
	
	return sumOfDigits

# Driven Program 
n = 4
print(squaresum(n)) 


