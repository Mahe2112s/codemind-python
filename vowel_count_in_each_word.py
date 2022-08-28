def string(str):
    a="aeiou"
    s=0
    for i in str:
        if i in a:
            s+=1
    if s==0:
        return '-1'
    else:
        return s
n=input()
for i in n.split():
    print(string(i),end=" ")