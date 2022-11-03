n,m=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in range(0,n):
    s=0
    for j in range(i,n):
        s+=x[j]
        if(s==m):
            c+=1
print(c)