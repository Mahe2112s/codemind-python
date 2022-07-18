def dig(n):
    c=0
    while n!=0:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
x=list(map(int,input().split()))
s=[]
c=0
for i in x:
    s.append(dig(i))
k=max(s)
for i in x:
    if dig(i)==k:
        c+=1
print(c)
        