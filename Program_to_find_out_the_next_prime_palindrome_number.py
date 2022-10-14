n=int(input())
def is_pal(s):
    t=s
    rev=0
    d=0
    while(s!=0):
       d=s%10
       s=s//10
       rev=rev*10+d
    if(rev==t):
        return 1
    else:
        return 0
def is_prime(s):
    if(s==1):
        return 0
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
            break
    else:
        return 1
n+=1
while(is_pal(n)==0 or is_prime(n)==0):
    n+=1
print(n)