def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
            
    return True
a=int(input())
c=0
d=len(str(a))
if(prime(a)):
    while a!=0:
        s=a%10
        a=a//10
        if(prime(s)):
            c+=1
    if(d==c):
        print('Mega Prime')
    else:
        print("Not Mega Prime")
else:
    print('Not Mega Prime')