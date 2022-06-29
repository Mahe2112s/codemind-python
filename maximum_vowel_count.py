n=input()
s=n.split()
c=[]
for i in s:
    v=sum(letter in'aeiou' for letter in i.lower())
    c.append(v)
print(max(c))