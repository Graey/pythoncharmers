arr = [1, 2, 3, 4, 5];      
n = 3;    
     
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i]),    

for i in range(0, n):    
     
    first = arr[0];    
        
    for j in range(0, len(arr)-1):    
        #Shift element of array by one    
        arr[j] = arr[j+1];    
             
    arr[len(arr)-1] = first;    
     
print();         
   
print("Array after left rotation: ");    
for i in range(0, len(arr)):    
    print(arr[i]),   
