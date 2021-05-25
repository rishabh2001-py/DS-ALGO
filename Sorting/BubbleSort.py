# --TIME COMPLEXITY-O(N*N)
# --BEST CASE- 0(N) if we give a sorted array  and provide a check after every inner loop so that loop can be terminated
#   in the case of 0 swap
#  --Worst Cae is o(n*n) when array is reversely sorted
def BubbleSort(arr):
    swap=0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if (arr[j + 1] < arr[j]):
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swap+=1
        if(swap==0):
            break
        count=0
        print(arr)


arr = list(map(int, input('Enter Array').strip().split()))
print("Before Sorting:", arr)
BubbleSort(arr)
print("After Sorting:", arr)
