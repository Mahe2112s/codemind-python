n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    l=len(str(i))
    if l%2==0:
        c+=1
print(c)