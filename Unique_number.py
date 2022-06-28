n=input()
s=[]
d=len(n)
for i in n:
    if i not in s:
        s.append(i)
if(len(s)==d):
    print('Unique Number')
else:
    print('Not Unique Number')
    
2nd Method 
n=input()
s=[]
d=len(n)
for i in n:
    if i not in s:
        s.append(i)
if(len(s)==d):
    print('Unique Number')
else:
    print('Not Unique Number')
