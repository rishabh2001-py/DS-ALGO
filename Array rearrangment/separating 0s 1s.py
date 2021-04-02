def sort012(arr, n):
    low = 0
    mid = 0
    high = n - 1
    while (mid <= high):
        if (arr[mid] == 0):
            arr[mid], arr[low] = arr[low], arr[mid]
            low = low + 1
            mid = high + 1
        elif (arr[mid] == 1):
            mid = mid + 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high=high-1
    return arr
arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(sort012(arr, n))
