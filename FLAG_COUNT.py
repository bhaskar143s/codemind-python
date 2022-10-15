a=int(input())
c=[]
fa=fb=2
fn=0
for i in range(a):
    c.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
print(c[a-1])