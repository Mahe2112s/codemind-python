n=input().lower()
n=n.split()
for i in n:
    for j in i:
        s=min(i)
        n=max(i)
    print(s,n,end=" ")