n=int(input())
l=list(map(int,input().split()))
m=int(input())
i=list(map(int,input().split()))
s=[]
for j in range(n):
    s.insert(i[j],l[j])
print(*s)