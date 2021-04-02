def rearrange(arr, n):
    arrb = n * [0]
    small = 0
    large = n - 1
    flag = True
    for i in range(0,n):
        if (flag == True):
            arrb[i] = arr[large]
            large = large - 1
            flag = False
        else:
            arrb[i] = arr[small]
            small = small + 1
            flag = True

    arr = arrb
    return arr


arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
arr = sorted(arr)
print(arr)
arr = rearrange(arr, n)
print(arr)
