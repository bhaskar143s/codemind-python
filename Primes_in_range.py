n=int(input())
m=int(input())
def is_prime(s):
    if(s==1):
        return 0
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
            break
    else:
        return 1
c=0
for i in range(n,m+1):
    if(is_prime(i)):
        c+=1
print(c)