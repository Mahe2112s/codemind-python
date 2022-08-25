n=input()
m=input()
n=n.lower()
m=m.lower()
s=0
for i in n.split():
    for j in m.split():
        if i==j:
            s+=1
print(s)