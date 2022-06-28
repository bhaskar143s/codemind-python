arr=list(map(int,input().split()))
m1=max(arr)
for i in range(0,len(arr)):
    if arr[i]==m1:
        arr[i]=0
m2=max(arr)
x=arr.count(0)
if x==2:
    print((m1-1)*(m1-1))
elif x==1:
    print((m1-1)*(m2-1))