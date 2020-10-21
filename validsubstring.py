#Given a string consisting of opening and closing parenthesis, find the #length(L) of the longest valid parenthesis substring.

count=0
tinplist=input()
inplist=list(tinplist)
for i in range((len(inplist)-1)):
    if inplist[i]=='(' and inplist[i+1]==')':
        count+=2
print(count)