def dig(n):
    c=0
    if n==0:
        return 1
    elif n<0:
        n = n*-1
    while(n):
        n=n//10
        c+=1
    return c
n=int(input())
x=list(map(int,input().split()))
b=[]
for i in x:
    b.append(dig(i))
for i in x:
    if dig(i)==max(b):
        print(i,end=" ")