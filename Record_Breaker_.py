import math
t=int(input())
for k in range(1,t+1):
    n=int(input())
    p=list(map(int,input().split()))
    c=0
    for j in range(n):
        if j==0:
            if p[j]>p[j+1]:
                c+=1
        elif j==n-1:
            f=0
            for i in range(n-1):
                if p[i]<p[j]:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                c+=1
        else:
            f=0
            for i in range(j):
                if p[j]>p[i]:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                if p[j]>p[j+1]:
                    c+=1
    print("Case #",end="")
    print(k,end="")
    print(":",end=" ")
    print(c)







