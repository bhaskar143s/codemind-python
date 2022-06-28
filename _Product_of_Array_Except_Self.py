n=int(input())
arr=list(map(int,input().split()))[:n]
l=[]
for i in range(0,len(arr)):
    p=1
    for j in range(0,len(arr)):
        if i!=j:
            p=p*arr[j]
            
    l.append(p)  
print(*l)