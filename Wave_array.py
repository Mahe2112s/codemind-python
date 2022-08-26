n=int(input())
x=list(map(int,input().split()))
for i in range(1,n-1,2):
    if(x[i-1]<x[i] and x[i]>x[i+1]) or (x[i-1]>x[i] and x[i]<x[i+1]):
        pass
    else:
        print('no')
        break
else:
    print('yes')