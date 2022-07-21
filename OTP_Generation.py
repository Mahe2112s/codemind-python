n=input()
a=n[::-1]
z=int(a)
while z!=0:
    e=z%10
    z=z//10
    if(e%2!=0):
        print(e*e,end="")
    