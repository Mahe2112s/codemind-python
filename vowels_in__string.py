n=input()
n=n.split()
s=[]
a="aeiouAEIOU"
f=0
for i in n:
    for j in i:
        if j in a and j not in s:
            s.append(j)
            f+=1
if(f==0):
    print('-1')
else:
    print(*s)