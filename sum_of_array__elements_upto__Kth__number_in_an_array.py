n=int(input())
x=list(map(int,input().split()))
a=int(input())
s=0
for i in x:
    s+=i
    if i==a:
        break
print(s)