n=int(input())
x=list(map(int,input().split()))
c,f=0,0
for i in range(n):
    if x[i]%2==0 and i%2==0:
        c+=1
    if x[i]%2==0:
        f+=1
if(f==c):
    print('True')
else:
    print('False')