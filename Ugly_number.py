def ugly(n):
    if n==0:
        return 0
    for i in[2,3,5]:
        while n%i==0:
            n=n//i
    return n==1
    
s=int(input())
if(ugly(s)):
    print("Ugly Number")
else:
    print("Not Ugly Number")