import sys 
A = [64, 25, 12, 22, 11] 
  
# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining unsorted array
    min_idx = i 	#it stores the index of minimum number
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 		#if we got a number less than current minimum we store that as minimum
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element of unsorted part of array   
    A[i], A[min_idx] = A[min_idx], A[i]


for i in range(len(A)): 
    print(A[i])   #printing sorted array
