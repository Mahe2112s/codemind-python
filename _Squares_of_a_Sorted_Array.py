n=int(input())
x=list(map(int,input().split()))
x.sort()
s=[]
for i in x:
    s.append(pow(i,2))
print(*sorted(s))