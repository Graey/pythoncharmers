import math

print("Enter your input format:")
print("1. a+ib")
print("2. r*e^(i*theta)")
print("3. rCis(theta)")

choice=int(input())

print("Enter number:")

if choice==1:
    print("Enter a:")
    a=float(input())
    print("Enter b:")
    b=float(input())
    r=math.sqrt(a*a+b*b)
    theta=math.atan(b/a)
elif choice==2:
    print("Enter r:")
    r=float(input())
    print("Enter theta:")
    theta=float(input())
    a=r*math.cos(theta)
    b=r*math.sin(theta)
elif choice==3:
    print("Enter r:")
    r=float(input())
    print("Enter theta:")
    theta=float(input())
    a=r*math.cos(theta)
    b=r*math.sin(theta)
else:
    print("wrong format!")

print(a,"+i",b)
print(r,"e^(i",theta,")")
print(r,"Cis",theta)
