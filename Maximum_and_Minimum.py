n=int(input())
a=list(map(int,input().split()))
f=0
s=[]
k=0
for i in range(n):
    if a[i]==a.count(a[i]) and a[i] not in s:
        s.append(a[i])
        f+=1
        k=1
if k==0:
    print(-1)
else:
 print(min(s),max(s))
