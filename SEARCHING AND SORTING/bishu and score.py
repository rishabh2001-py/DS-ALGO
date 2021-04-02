
def fun(arr,n,m):
    prefix=[]
    add=0
    arr.sort()
    for i in range(0,n):
        add=add+arr[i]
        prefix.append(add)
    if(m==0):
        print(0,0)
        return
    if(m>n):
        print(n,prefix[n-1])
        return
    high=n-1
    low=0
    while(low<high):
        mid=int(high+low//2)
        if(arr[mid]>m):
            high=mid-1
        elif(arr[mid]<m):
            low=low+1
        elif(arr[mid]==m):
            return mid
    print(mid+1,prefix[mid])






n=int(input("size"))
arr=list(map(int,input("arr::").strip().split()))
m=int(input("power:"))
fun(arr,n,m)



