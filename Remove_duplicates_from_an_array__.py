n=int(input())
arr=list(map(int,input().split()))[:n]
res=[]
[res.append(x) for x in arr if x not in res]
print(*res)