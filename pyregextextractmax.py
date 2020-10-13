# Function to extract maximum numeric value from 
# a given string 
import re 

def extractMax(input): 

	# get a list of all numbers separated by 
	# lower case characters 
	# \d+ is a regular expression which means 
	# one or more digit 
	# output will be like ['100','564','365'] 
	numbers = re.findall('\d+',input) 

	# now we need to convert each number into integer 
	# int(string) converts string into integer 
	# we will map int() function onto all elements 
	# of numbers list 
	numbers = map(int,numbers) 

	print max(numbers) 

# Driver program 
if __name__ == "__main__": 
	input = '100klh564abc365bg'
	extractMax(input) 
