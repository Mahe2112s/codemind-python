n=input()
s=[]
c=0
for i in n.split():
    s.append(len(i))
print(max(s))