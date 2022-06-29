n=int(input())
x=list(map(int,input().split()))
a=int(input())
s=0
for i in x:
    if i==a:
        s+=1
print(s)
    