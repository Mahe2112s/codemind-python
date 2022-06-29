n=input()
s=[]
for i in n:
    if n.count(i)==1:
        s.append(i)
if(len(s)==0):
    print("-1")
else:
    print(s[0])