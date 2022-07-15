def fck(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s
n=int(input())
x=list(map(int,input().split()))
s=[]
for i in x:
    s.append(fck(i))
print(sum(s))