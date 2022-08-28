n=input()
s=[]
n=n.lower()
a="abcdefghijklmnopqrstuvwxyz0123456789 "
for i in n:
    if i not in a:
        s.append(i)
print(len(s))