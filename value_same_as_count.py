n=int(input())
x=list(map(int,input().split()))
c=0
for i in sorted(set(x)):
    if x.count(i)==i:
        c+=1
print(c)