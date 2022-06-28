n=int(input())
arr=list(map(int,input().split()))[:n]
ev=od=0
for i in range(0,len(arr)):
    if arr[i]%2==0:
        ev+=1
    elif arr[i]%2!=0:
        od+=1
print(ev,od)