n=int(input())
x=list(map(int,input().split()))
s=[]
for i in x:
    if i not in s:
        s.append(i)
print(sum(s))