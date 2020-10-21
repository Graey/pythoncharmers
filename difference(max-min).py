#Given an array A of integers and an integer K, add any K elements of A #to form the maximum(max) sum and the minimum(min) sum and Find D(max-min).

inp=[int(x) for x in (input().split(" "))]
n=inp[0]
k=inp[-1]
arrn=[int(x) for x in (input().split(" "))]
arr=[int(x) for x in arrn]
sortedrray=sorted(arr)
maxsum=0
minsum=0
for x in sortedrray[0:k]:
    minsum+=x
for x in sortedrray[-1:-k-1:-1]:
    maxsum+=x
print(maxsum-minsum)