n=int(input())
sq=n*n
sum=0
while(sq>0):
    a=sq%10
    sum=sum+a
    sq=sq//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")
    