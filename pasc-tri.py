M = int(input())
a=[[] for i in range(M)]
def pascal_triangle(M):

    for i in range(M):
        for j in range(i+1):
            if(j<i):
                if(j==0):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif(j==i):
                a[i].append(1)


pascal_triangle(M)
for i in range(M):
    for j in range(i+1):
        print("{} ".format(a[i][j]), end="")
    print(" ")
