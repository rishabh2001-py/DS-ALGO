def doublethefirst(arr, n):
    for i in range(0, n - 1):
        if (arr[i] != 0 and arr[i + 1] != 0):
            arr[i] = arr[i] * 2
            arr[i + 1] = 0
    s = -1
    j = 0
    for j in range(0, n):
        if (arr[j] != 0):
            s = s + 1
            arr[j], arr[s] = arr[s], arr[j]
    return arr


# 0, 2, 2, 2, 0, 6, 6, 0, 0, 8


arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(doublethefirst(arr, n))
