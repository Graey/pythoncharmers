# Python program to print Even Numbers in given range 

start = int(input("Enter the start of range: ")) 
end = int(input("Enter the end of range: ")) 

# iterating each number in list 
for num in range(start, end + 1): 
	
	# checking condition 
	if num % 2 != 0: 
		print(num, end = " ") 
