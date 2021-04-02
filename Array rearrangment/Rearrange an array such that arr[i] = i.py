





def rearange(arr,n):
    s=set(arr)
    print(s)
    for i in range(0,n):
        if i in s:
            arr[i]=i
        else:
            arr[i]=-1
    return  arr















arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(rearange(arr,n))