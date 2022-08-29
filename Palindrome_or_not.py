def string(str):
    return str[::-1]
n=input().lower()
if n==string(n):
    print('True')
else:
    print('False')