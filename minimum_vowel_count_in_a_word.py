n=input()
n=n.lower()
a="aeiou"
s=[]
c=0
for i in n.split():
    for j in i:
        if j in a:
            c+=1
    s.append(c)
    c=0
m=min(s)
print(m)
        