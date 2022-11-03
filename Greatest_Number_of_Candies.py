n=int(input())
x=list(map(int,input().split()))
a=int(input())
k=max(x)
s=0
for i in x:
    s+=(i+a)
    if(s>=k):
        print("True",end=" ")
    else:
        print("False",end=" ")
    s=0