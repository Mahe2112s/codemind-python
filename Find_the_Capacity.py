a,b,c=map(int,input().split())
x=2*a*b*c*512
b=x//1024
print("{0}KB".format(b))