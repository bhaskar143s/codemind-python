a,b=map(int,input().split())
s=[list(map(int,input().split()))for i in range(a)]
for j in range(b):
    d=[]
    for i in range(a):
        d.append(s[i][j])
    print(max(d))