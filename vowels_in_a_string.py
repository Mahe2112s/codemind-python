n=input()
a="aeiouAEIOU"
c=0
k=input()
for i in n:
    if i in k:
        c=1
if c==1:
    print('True')
    print(n.index(k))
else:
    print('False')