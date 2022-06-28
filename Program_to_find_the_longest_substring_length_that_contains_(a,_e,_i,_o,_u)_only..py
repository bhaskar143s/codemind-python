a=input().lower()
c=x=0
vow=set("aeiou")
a=list(a)
for i in range(len(a)):
    c=0
    for j in range(i,len(a),1):
        if a[j] in vow:
            c+=1
            if x<c:
                x=c
        else:
            break
print(x)