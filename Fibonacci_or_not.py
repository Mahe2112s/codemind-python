n=int(input())
if n==0:
    print('True')
elif(n==1):
    print('True')
else:
    a=0
    b=1
    c=a+b
    while(c<n):
        c=a+b
        a=b
        b=c
    if(c==n):
        print('True')
    else:
        print('False')