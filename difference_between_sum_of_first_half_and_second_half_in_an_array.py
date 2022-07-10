n=int(input())
x=list(map(int,input().split()))
b=n//2
s=0
c=0
for i in range(0,b):
    s+=x[i]
for j in range(n-1,b-1,-1):
    c+=x[j]
print(abs(s-c))