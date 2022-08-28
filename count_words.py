n=input()
n=n.lower()
n=n.split()
c=0
for i in n:
    if i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u':
        if(i[len(i)-1]!='a' or i[len(i)-1]!='e' or i[len(i)-1]!='i' or i[len(i)-1]!='o' or i[len(i)-1]!='u'):
            c+=1
print(c)