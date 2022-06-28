def isogram(str1):
    if (len(str1)==len(set(str1.lower()))):
        return True
    return False
a=input()
print(isogram(a))