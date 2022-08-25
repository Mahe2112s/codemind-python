n=input().lower()
m=input().lower()
for i in m.split():
    for j in n.split():
        if i==j:
            print(i,end=" ")