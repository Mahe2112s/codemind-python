n=int(input())
s=0
d=0
l=0
while n!=0:
    r=n%10
    n=n//10
    d=d*10+r
while d!=0:
    p=d%10
    if p==6 and s==0:
        p=9
        s+=1
    l=l*10+p
    d=d//10
print(l)
