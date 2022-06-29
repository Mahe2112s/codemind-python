n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    c+=i
s=c//n
for i in x:
    if i==s:
        print('True')
        break
else:
    print('False')