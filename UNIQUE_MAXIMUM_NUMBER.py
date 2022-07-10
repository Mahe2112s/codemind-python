n=int(input())
x=list(map(int,input().split()))
s=[]
f=0
for i in range(0,n):
    if x.count(x[i])==1:
        s.append(x[i])
        f=1
if(f==0):
    print('-1')
else:
    print(max(s))
