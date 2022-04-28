n=int(input())
a=0
while n>0:
    r=n%10
    if a<r:
        a=r
    n=n//10
print(a)