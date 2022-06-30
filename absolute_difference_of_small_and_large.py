s=input()
a=list(s.split())
x=c=0
for i in a:
    ma='z'
    mi='A'
    for j in i:
        if ord(j)<ord(ma):
            ma=j
        if ord(j)>ord(mi):
            mi=j
    print(ord(mi)-ord(ma),end=" ")


