n=int(input())
arr=list(map(int,input().split()))[:n]
arr1=list(map(int,input().split()))[:n]
zip_list=zip(arr,arr1)
sum = [x + y for (x, y) in zip_list]
print(*sum)