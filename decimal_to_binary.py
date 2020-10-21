a=float(input("Enter decimal number to be converted :"))
print(a)
arr=[]
while a>1  :
	if a%2==0.0:
		arr.append('0')
		a=a/2
	else :
		arr.append('1')
		a=a-1
		a=a/2

arr.append('1')
arr=arr[::-1]
 
def listToString(arr):  
    str1 = ""  
    for ele in arr:  
        str1 += ele   
    return str1  
    int(str1)
     

print("Your converted decimal in binary is : ",arr ,"\nthat is :",listToString(arr) )