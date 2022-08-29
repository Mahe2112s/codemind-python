n=input()
n=n.split()
z=0
x=0
for i in n:
    s=ord(min(i))
    n=ord(max(i))
    z+=s
    x+=n
    d=abs(z-x)
print(d)
    