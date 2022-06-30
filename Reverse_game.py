def pal(n):
    c=0
    while(n>0):
        d=n%10
        n=n//10
        c=c*10+d
    return c
a=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    print(pal(i),end=' ')