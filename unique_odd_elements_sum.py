n=int(input())
a=list(map(int,input().split()))
c=0
s=set(a)
z=list(s)
for i in z:
    if i%2!=0:
        c+=i
print(c)