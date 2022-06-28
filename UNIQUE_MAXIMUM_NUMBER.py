n=int(input())
max=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    c=0
    for j in range(0,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
            break
    if(c==0):
            if(arr[i]>max):
               max=arr[i]
if(max==0):
    print(-1)
else:
    print(max)