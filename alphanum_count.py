num = 0
char = 0
sent = input("Enter any Alphanumeric String: ")
if len(sent)!=0:
    for i in sent:
        if i.isalpha():
            char += 1

        elif i.isnumeric():
            num += 1

else:
    print("Please give an input!")

print("Letter: {}".format(char))
print("Digits: {}".format(num))
