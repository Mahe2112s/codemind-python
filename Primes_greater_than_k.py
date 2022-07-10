def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
n=int(input())
x=list(map(int,input().split()))
a=int(input())
c=0
for i in x:
    if prime(i):
        if i>=a:
            c+=1
print(c)