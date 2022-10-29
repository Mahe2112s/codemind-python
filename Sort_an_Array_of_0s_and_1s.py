n=int(input())
x=list(map(int,input().split()))
for i in range(0,n):
    if(x[i]!=1):
        print("0",end=" ");
for i in range(0,n):
    if(x[i]==1):
        print(x[i],end=" ");