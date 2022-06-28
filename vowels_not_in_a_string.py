n=input()
s=[]
a='aeiou'
for i in a:
    if i not in n:
        s.append(i)
if(len(s)==0):
    print('0')
else:
    for j in s:
        print(j,end=" ")