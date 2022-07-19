n=input()
c=0
a=input()
for i in n:
    if i==a:
        c+=1
if(c==0):
    print('-1')
else:
    print(c)