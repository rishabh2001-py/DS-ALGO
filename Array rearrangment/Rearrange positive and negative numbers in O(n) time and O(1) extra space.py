#  Python program to put positive numbers at even indexes (0,  // 2, 4,..) and
#  negative numbers at odd indexes (1, 3, 5, ..)
def rearrangePosAND(arr,n):
    i=-1
    for j in range(n):
        if(arr[j]<0):
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    print(arr)

    pos = i + 1
    neg = 0
    while (pos < n and neg < pos and arr[neg] < 0):
        arr[pos], arr[neg] = arr[neg], arr[pos]
        pos = pos + 1
        neg = neg + 2
    return arr






















arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(rearrangePosAND(arr,n))




