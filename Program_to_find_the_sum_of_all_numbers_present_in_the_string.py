def sum(str1):
    c=0
    for i in str1:
        if i.isdigit():
            z=int(i)
            c+=z
    return c
s=input()
print(sum(s))