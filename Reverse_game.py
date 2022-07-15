def pal(n):
    d=0
    while(n!=0):
        r=n%10
        n=n//10
        d=d*10+r
    return d
n=int(input())
x=list(map(int,input().split()))
for i in x:
    print(pal(i),end=" ")