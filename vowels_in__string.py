n=input()
s=''
a='aeiouAEIOU'
f=0
for i in n:
    if i in a and i not in s:
        s+=i
        f=1
if(f==1):
    print(*s)
else:
    print(-1)