n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=0
for i in list(set(x)):
    if y.count(i)==0:
        c+=1
for j in list(set(y)):
    if x.count(j)==0:
        c+=1
print(c)