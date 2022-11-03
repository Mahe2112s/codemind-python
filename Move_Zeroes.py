n=int(input())
x=list(map(int,input().split()))
for i in x:
    if(i!=0):
        print(i,end=" ")
for i in x:
    if(i==0):
        print(i,end=" ")