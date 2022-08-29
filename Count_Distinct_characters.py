def string(str):
    return ''.join(sorted(str))
n=input()
n=n.lower()
s=[]
for i in n:
    if i==' ':
        continue
    else:
        if i not in s:
            s.append(i)
print(len(s))
        