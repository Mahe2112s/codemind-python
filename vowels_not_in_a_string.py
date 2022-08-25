n=input()
a='aeiou'
n=n.lower()
s=[]
f=[]
for i in a:
    if i not in n:
        f.append(i)
if len(f)==0:
    print('0')
else:
    print(*f)