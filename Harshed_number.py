n=int(input())
a=n
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
if(a%s==0):
    print('True')
else:
    print('False')