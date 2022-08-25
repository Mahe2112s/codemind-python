n=input()
s=[]
n=n.lower()
for i in n:
    if i==' ':
       continue
    if i not in s:
        s.append(i)
print(len(s))