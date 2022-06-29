n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    c+=i
s=c/n
print('%.2f'%s)