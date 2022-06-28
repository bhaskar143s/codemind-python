def move(arr):
    l=len(arr)
    c=0
    for i in range(l):
       if arr[i]!=0:
           arr[c]=arr[i]
           c+=1
    while c<l:
        arr[c]=0
        c+=1
    return arr
n=int(input())
arr=list(map(int,input().split()))[:n]
print(*move(arr))