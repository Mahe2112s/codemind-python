n=input()
s=[]
l='aeiou'
for i in n:
    if i in l:
        if i not in s:
            s.append(i)
if(len(s)==len(l)):
    print('True')
else:
    print('False')