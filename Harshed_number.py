n=int(input())
s=n
a=0
while n>0:
    r=n%10
    a=a+r
    n=n//10
if(s%a==0):
    print('True')
else:
    print('False')