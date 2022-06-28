n=int(input())
x=0
arr=list(map(int,input().strip().split()))[:n] 
for i in range(0,len(arr)):
    v=0
    while(arr[i]!=0):
        d=arr[i]%10
        arr[i]=arr[i]//10
        v+=1
    if(v%2==0):
        x+=1
print(x)