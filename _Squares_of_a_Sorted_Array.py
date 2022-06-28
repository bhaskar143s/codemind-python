n=int(input())
arr=list(map(int,input().split()))[:n]
for i in range(0,len(arr)):
    if arr[i]<0:
        arr[i]=abs(arr[i])
arr.sort()
for i in range(0,len(arr)):
    arr[i]=arr[i]**2
print(*arr)