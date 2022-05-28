n=int(input())
l=len(str(n))
s=n**2
d=s%pow(10,l)
if d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")