n=int(input())
x=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,n):
    if x[i]>k:
        break
    else:
        c+=x[i]
print(c)