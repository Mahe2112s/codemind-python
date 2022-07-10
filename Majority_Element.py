n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    if x.count(x[i])>n//2:
        print(x[i])
        break