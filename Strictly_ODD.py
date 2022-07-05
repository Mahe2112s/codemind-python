n=int(input())
x=list(map(int,input().split()))
f=0
c=0
for i in range(0,n):
    if x[i]%2!=0 and i%2!=0:
        f+=1
    if x[i]%2!=0:
        c+=1
if(f==c):
    print('True')
else:
    print('False')