n=input()
z=n.split()
c=0
for i in z:
    if c%2==0:
        print(i[::-1],end=" ")
    else:
        print(i,end=" ")
    c+=1

