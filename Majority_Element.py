n=int(input())
arr=list(map(int,input().split()))[:n]
max=0
for i in range(0,len(arr)):
    c=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if c>max:
        max=c
        p=arr[i]
print(p)