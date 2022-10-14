def is_prime(s):
    if(s==1):
        return 0
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
            break
    else:
        return 1
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if(is_prime(i)==0):
            c+=1
print(c)