for i in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))[:n]
    arr1=list(map(int,input().split()))[:m]
    new_arr=arr+arr1
    new_arr.sort()
    print(*new_arr)