n=int(input())
x=list(map(int,input().split()))
s=[]
f=0
for i in x:
    if x.count(i)==i:
        s.append(i)
        f=1
if f==0:
    print('-1')
else:
    b=set(s)
    l=sum(b)
    a=len(b)
    print("%.2f"%(l/a))
        