def string(str):
    return ''.join(sorted(str))
n=input()
s=[]
for i in n:
    if i not in s:
        s.append(i)
a=string(s)
print(max(a))