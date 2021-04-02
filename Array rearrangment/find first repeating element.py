
def firstRepeated(arr, n):
    dic={}
    for i in range(n):
        dic[arr[i]]=0
    print(dic)
    for i in range(n):
        dic[arr[i]]=dic[arr[i]]+1
    print(dic)
    for i in range(0,n):
        if(dic[arr[i]]>1):
            return i+1
    return -1



arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(firstRepeated(arr,n))