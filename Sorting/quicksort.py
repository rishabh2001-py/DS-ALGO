def quicksort(arr, n, low, high):

    if (low < high):
        pivot = partition(arr, high, low)
        quicksort(arr,n, low, pivot - 1)
        quicksort(arr, n,pivot + 1, high)
    return arr


def partition(arr, high, low):
    pivot = low
    while (low < high):
        while arr[low] < arr[pivot]:
            low = low + 1
        while arr[high] > arr[pivot]:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]
    pivot = high
    return pivot


arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(quicksort(arr,n,0,n-1))


#10, 80, 30, 90, 40, 50, 70