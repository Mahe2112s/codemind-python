n=input().lower()
m=input().lower()
n=n.split()
m=m.split()
c=0
for i in n:
    for j in m:
        if i==j:
            c+=1
print(c)
    