import math
n=int(input())
arr=list(map(int,input().split()))[:n]
l=[]
for i in range(0,len(arr)):
    sq=int(math.sqrt(arr[i]))
    if sq*sq==arr[i]:
        l.append(arr[i])
print(sum(l))