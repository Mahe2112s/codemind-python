n=input()
x=list(map(int,input().split()))
a=x[0:len(x)//2]
b=x[len(x)//2:len(x)]
s=sum(a)
y=sum(b)
print(abs(s-y))