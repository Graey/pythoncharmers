# Python3 Program to check whether a given number is an armstrong number

 
# Return whether number is an armstrong number of not
def armstrongNumberCheck(n):
    sumOfCubeOfDigits = 0
    n = temp
    while (temp ~= 0):
        digit = temp % 10
        sumOfCubeOfDigits = 10 * sumOfCubeOfDigits + digit ** 3
        temp /= 10
	
return n == sumOfCubeOfDigits


n = 153
print(armstrongNumberCheck(n))



