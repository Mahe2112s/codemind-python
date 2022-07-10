n=int(input())
x=list(map(int,input().split()))
s=0
e=0
for i in range(0,n):
    if i%2==0:
        e+=x[i]
    else:
        s+=x[i]
if(abs(s-e)==0):
    print('YES')
else:
    print('NO')
    