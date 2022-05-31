a,b=map(int,input().split())
for i in range(1,b+1):
    if i%2==0:
        continue
    else:
        print('{0} x {1} = {2}'.format(a,i,a*i))

    
