n=int(input())
a=n
d=0
if n<0:
    n=-n
while n>0:
    r=n%10
    d=d*10+r
    n=n//10
if(a<0):
    print(-d)
else:
    print(d)