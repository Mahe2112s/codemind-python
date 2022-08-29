def string(str):
    return ''.join(sorted(str))
n=input().lower()
m=input().lower()
s=[]
for i in n:
    if i==' ':
        continue
    if i  in m and i not in s:
        s.append(i)
for i in m:
    if i==' ':
        continue
    if i in n and i not in s:
        s.append(i)
print(len(s))
        