n=int(input())
x=list(map(int,input().split()))
s=[]
c=0
for i in x:
    if i not in s:
        s.append(i)
for i in s:
    if i%2!=0:
        c+=1
print(c)
        