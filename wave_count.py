n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(1,n-1,2):
    if(x[i-1]<x[i] and x[i]>x[i+1]):
        c+=1
    else:
        print('-1')
        break
else:
    print(c)