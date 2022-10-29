n=int(input())
x=list(map(int,input().split()))
for i in range(0,n):
    pro=1
    for j in range(0,n):
        if(i!=j):
            pro=pro*x[j]
    print(pro,end=" ")