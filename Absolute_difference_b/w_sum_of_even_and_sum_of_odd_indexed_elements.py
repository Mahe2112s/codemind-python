n=int(input())
a=list(map(int,input().split()))
e=0
s=0
for i in range(0,n):
    if  i%2==0:
        e+=a[i]
    else:
        s+=a[i]
print(abs(e-s))