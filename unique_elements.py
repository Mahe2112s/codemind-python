n=int(input())
s=[]
x=list(map(int,input().split()))
for i in x:
    if i not in s:
        s.append(i)
print(*s)