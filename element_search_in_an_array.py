n=int(input())
x=list(map(int,input().split()))
se=int(input())
for i in x:
    if i==se:
        print('True')
        break
else:
    print('False')