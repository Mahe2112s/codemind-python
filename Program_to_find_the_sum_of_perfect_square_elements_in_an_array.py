n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    for j in range(1,a[i]+1):
        if a[i]==j*j:
            s+=a[i]
print(s)
    