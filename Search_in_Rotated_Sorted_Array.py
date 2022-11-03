n=int(input())
x=list(map(int,input().split()))
a=int(input())
f=0
for i in range(0,n):
    if(x[i]==a):
        print(i)
        f=1
if(f==0):
    print("-1")