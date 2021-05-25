def InsertionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]
        print("Array After", i ,"sort",arr)


arr = list(map(int, input('Enter Array').strip().split()))
print("Before Sorting:", arr)
InsertionSort(arr)
print("After Sorting:", arr)
