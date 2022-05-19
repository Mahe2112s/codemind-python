n=int(input())
d=len(str(n))
a=n
s=0
while n:
    r=n%10
    n=n//10
    l=pow(r,d)
    s+=l
    d-=1
if (s==a):
    print('True')
else:
    print('False')