n=int(input())
arr=list(map(int,input().split()))[:n]
d=0
l=[]
for i in range(n):
    c=arr.count(arr[i])
    if c>d:
        d=c
for i in range(n):
    if arr.count(arr[i])==d:
        l.append(arr[i])
s=set(l)
if len(s)>1:
    print(min(s))
else:
    print(*s)