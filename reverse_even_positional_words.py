def string(str):
    return str[::-1]
n=input().lower()
n=n.split()
for i in range(len(n)):
    if i%2==0:
        print(string(n[i]),end=" ")
    else:
        print(n[i],end=" ")