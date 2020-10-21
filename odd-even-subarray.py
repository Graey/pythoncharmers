n=int(input())
arr=list(map(int, input().split()))
pos=[0 for i in range(n+1)]
neg=[0 for i in range(n+1)]
itr=0
res=0
pos[0]=1

for i in arr:
    if i%2==0:
        itr+=1
    else:
        itr-=1
    if itr<0:
        res+=neg[-itr]
        neg[-itr]=neg[-itr]+1
    else:
        res+=pos[itr]
        pos[itr]=pos[itr]+1
print(res)