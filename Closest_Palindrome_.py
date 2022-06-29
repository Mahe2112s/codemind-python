def pal(n):
    c=0
    while(n>0):
        d=n%10
        n=n//10
        c=c*10+d
    return c
a=int(input())
temp=a
if(a==pal(a)):
    t=a-1
    temp=a+1
    for i in range(t,1,-1):
        if(i==pal(i)):
            p=i
            break
    while(temp!=0):
        if(temp==pal(temp)):
            q=temp
            break
        temp+=1
else:
    for i in range(a,1,-1):
        if(i==pal(i)):
            p=i
            break
    while(temp!=0):
        if(temp==pal(temp)):
            q=temp
            break
        temp+=1
if((a-p)<(q-a)):
    print(p)
elif((a-p)==(q-a)):
    print(p,q)
else:
    print(q)