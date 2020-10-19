import string  # import ascii_uppercase

# num = int(input("Enter the number of rows: "))
num = 5
for i in range(1, num + 1):
    # for j in range(i):
    print("* " * i)
# print(" ")
print("\n---------------------------------------------\n")
num = 7
for i in range(num, 0, -1):
    # for j in range(i):
    print("* " * i)
# print(" ")
print("\n---------------------------------------------\n")
num = 1
for i in range(5):
    for j in range(i + 1):
        print(num, end=" ")
    num += 1
    print(" ")
print("\n---------------------------------------------\n")
num = 4
for i in range(1, num + 1):
    for j in range(i):
        print("*\t", end="")
    print(" ")
print("\n---------------------------------------------\n")
num = 1
for i in range(4):
    for j in range(i + 1):
        print("%d " % num, end="")
        num += 1
    print()
print("\n---------------------------------------------\n")
num = 0
for i in range(6):
    if i == 4:
        continue
    for j in range(i):
        if i == 4:
            continue
        print(string.ascii_uppercase[num], end=" ")
        num += 1
    print(" ")
