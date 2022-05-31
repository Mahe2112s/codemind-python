def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r
n=int(input())
a=n
s=0
while a!=0:
    f=a%10
    s=s+fact(f)
    a=a//10
if(s==n):
    print('The number {0} is a strong number'.format(n))
else:
    print('The number {0} is not a strong number'.format(n))
