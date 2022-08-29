def string(str):
    return str[::-1]
n=input().lower()
c=0
n=n.split()
for i in n:
    if i==string(i):
        c+=1
print(c)