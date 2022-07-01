n=int(input())
p=list(map(int,input().split()))
for i in range(n-1,(n//2)-1,-1):
    print(p[i],end=" ")
for j in range(0,n//2):
    print(p[j],end=" ")

