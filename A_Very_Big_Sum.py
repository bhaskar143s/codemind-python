n=int(input())
p=list(map(int,input().split()))
res=0
res=p[0]
for i in range(1,n):
    res=res+p[i]
print(res)
