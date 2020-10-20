
def bubbleSort(arr): 
	n = len(arr) 

	# Traverse through all array elements 
	for i in range(n-1): 

		# Last i elements are already in place 
		for j in range(0, n-i-1): 

			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

# Driver code 
arr = [94, 34, 28, 15, 27, 10, 99] 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 
