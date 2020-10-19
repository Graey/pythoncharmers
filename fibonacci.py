n = int(input("Enter total number of elements: "))
a = 0
b = 1
nth = 0
if (n > 0):
    for i in range(n):
        print(nth)
        a = b
        b = nth
        nth = a+b

else:
    print("Enter a Positive and Non-zero number!")



