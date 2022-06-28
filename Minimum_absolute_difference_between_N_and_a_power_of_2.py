from math import floor,log2
def minabs(n):
    l=pow(2,floor(log2(n)))
    r=l*2
    return min((n-l),(r-n))
a=int(input())
print(minabs(a))