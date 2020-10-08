# Python code to demonstrate defaultdict 

# importing "collections" for defaultdict 
import collections 

# declaring defaultdict 
# sets default value 'Key Not found' to absent keys 
defd = collections.defaultdict(lambda : 'Key Not found') 

# initializing values 
defd['a'] = 1

# initializing values 
defd['b'] = 2

# printing value 
print ("The value associated with 'a' is : ",end="") 
print (defd['a']) 

# printing value associated with 'c' 
print ("The value associated with 'c' is : ",end="") 
print (defd['c']) 
