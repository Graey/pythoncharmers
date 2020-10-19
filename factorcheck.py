a, b = map(int,input("Enter two numbers: ").split())
if(b>a):
    print("{} is not a factor of {}".format(b, a))

elif(a%b==0):
    print("{} is a factor of {}".format(b, a))

else:
    print("{} is not a factor of {}".format(b, a))
