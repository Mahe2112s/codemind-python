n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
k=list(set(x).intersection(y))
print(len(k))