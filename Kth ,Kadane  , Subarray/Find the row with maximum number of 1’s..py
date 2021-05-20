import  sys
def MaxnumofROW(arr,n,m):
    count=0
    rownum=-3
    maxrow=-sys.maxsize
    for i in range(0,n):
        count=0
        for j in range(0,m):
            if(arr[i][j]==1):
                count=count+1
        if(count>maxrow):
            maxrow=count
            rownum=i+1
    print(maxrow)
    print(rownum)


















n=int(input("Enter Row::"))
m=int(input("Enter Column::"))
arr=[]
for i in range(0,n):
    a=[]
    for j in range(0,m):
        a.append(int(input()))
    arr.append(a)
i=j=0
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()

MaxnumofROW(arr,n,m)



