n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=[]
for i in x:
    if i in y and i not in a:
        a.append(i)
print(*a)