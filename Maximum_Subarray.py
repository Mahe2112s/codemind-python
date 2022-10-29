n=int(input())
x=list(map(int,input().split()))
max=-100
for i in range(0,n):
    s=0
    for j in range(i,n):
        s+=x[j]
        if(s>max):
            max=s
print(max)