x=[]
for i in range(int(input())):
    n=int(input())
    x.append(n)
y=int(input())
t=0
for i in range(0,len(x)):
    if(x[i]<=y):
        t+=1
    else:
        t+=2
print(t)

    