n=int(input())
for i in range(n):
    def se(n):
        a=n[::-1]
        return a
    def dig(n):
        l=len(n)
        return l
    a=input()
    if a==se(a) and dig(a)%2==0:
        print('YES','EVEN')
    elif a==se(a) and dig(a)%2!=0:
        print('YES','ODD')
    else:
        print('NO')