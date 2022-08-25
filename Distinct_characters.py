def string(str):
    return ''.join(sorted(str))

n=input()
s=[]
for i in n.lower():
    if i==' ':
        continue
    if n.count(i)==1:
        s.append(i)
print(string(s))