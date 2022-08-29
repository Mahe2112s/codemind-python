n=input().lower()
n=n.split()
for i in n:
    s=min(i)
    n=max(i)
    print(s,n,end=" ")