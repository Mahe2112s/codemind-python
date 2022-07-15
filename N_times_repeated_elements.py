n=int(input())
x=list(map(int,input().split()))
a=int(input())
s=[]
f=0
for i in sorted(set(x)):
    if x.count(i)==a:
        s.append(i)
        f=1
if(f==0):
    print('-1')
else:
    print(*s)