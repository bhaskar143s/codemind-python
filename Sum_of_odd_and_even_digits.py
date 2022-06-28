n=int(input())
Even=0
Odd=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    if i%2==0:
        Even=Even+arr[i]
    elif i%2!=0:
        Odd=Odd+arr[i]
if (Odd-Even)==0:
    print("YES")
else:
    print("NO")