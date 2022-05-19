n=int(input())
for i in range(1,n+1):
    a=int(input())
    for j in range(1,a+1):
        if(a==j*j):
            print("True")
            break
    else:
        print("False")