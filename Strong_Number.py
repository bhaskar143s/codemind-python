def strong(d):
    fac=1
    for i in range(1,d+1):
        fac=fac*i
    return fac
n=int(input())
x=n
sum=0
while n!=0:
    d=n%10
    sum+=strong(d)
    n=n//10
if sum==x:
    print("The number {} is a strong number".format(x))
else:
    print("The number {} is not a strong number".format(x))