x=list(map(int,input().split()))
y=max(x)
z=min(x)
x[x.index(y)]=z
s=max(x)
print((y-1)*(s-1))