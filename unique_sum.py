n=int(input())
a=list(map(int,input().split()))
c=0
s=set(a)
z=list(s)
for i in z:
    c+=i
print(c)
