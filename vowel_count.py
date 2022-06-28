n=input()
s='aeiouAEIOU'
c=[]
for i in n:
    if i in s:
        c.append(i)
if(len(c)==0):
    print('0')
else:
    print(len(c))
    

