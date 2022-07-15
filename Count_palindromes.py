def pal(n):
    d=0
    while(n!=0):
        r=n%10
        n=n//10
        d=d*10+r
    return d
n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if i==pal(i):
        c+=1
print(c)