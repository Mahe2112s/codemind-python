n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=a
    d=0
    while a:
        r=a%10
        a=a//10
        d=d*10+r
    if d==b:
        print('True')
    else:
        print('False')
        
