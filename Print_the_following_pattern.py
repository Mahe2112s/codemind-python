n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
print()
for i in range(2,n+1):
    for j in range(2,n+1):
        if i==j or j>=i:
            print(j,end=" ")
    print()