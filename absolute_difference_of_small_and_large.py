n=input()
n=n.split()
for i in n:
    s=ord(min(i))
    n=ord(max(i))
    y=abs(s-n)
    print(y,end=" ")