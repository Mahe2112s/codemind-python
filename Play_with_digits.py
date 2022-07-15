def dig(n):
    c=0
    while(n!=0):
        r=n%10
        c+=r
        n=n//10
    return c
n=int(input())
x=list(map(int,input().split()))
s=[]
c=0
for i in x:
    s.append(dig(i))
print(sum(s))
    