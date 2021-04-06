

a=int(input("number"))
a=str(a)
print((a))
flag=1
for i in range(0,len(a)//2):
    if(a[i]!=a[len(a)-1-i]):
        flag=0
        break
print(flag)
s=""
j=0
for i in range(len(a)-1,-1,-1):
    s=s+a[i]
    j=j+1
print(s)



