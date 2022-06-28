n=int(input())
arr=list(map(int,input().split()))[:n]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j] and i!=j:
            print(arr[i])