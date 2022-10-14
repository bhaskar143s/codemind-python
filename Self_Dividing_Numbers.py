n=int(input())
m=int(input())
for i in range(n,m+1):
    d=0
    p=i
    s=0
    c=0
    while(i!=0):
        d=i%10
        i=i//10
        s+=1
        if(d==0):
            break
        if(p%d==0):
            c+=1
    if(s==c):
        print(p,end=" ")