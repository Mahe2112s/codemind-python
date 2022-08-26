n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(2,n):
    if(x[i-1]+x[i-2])==x[i]:
        c=1
    else:
        c=0
        break
if(c==0):
    print('no')
else:
    print('yes')