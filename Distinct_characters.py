def string(str):
    return ''.join(sorted(str))

n=input()
s=[]
for i in n.lower():
    if i==' ':
        continue
    if i not in s:
        s.append(i)
print(string(s))