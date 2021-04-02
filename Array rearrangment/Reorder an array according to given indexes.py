# Input:  arr[]   = [10, 11, 12];
# index[] = [1, 0, 2];
# Output: arr[]   = [11, 10, 12]
# index[] = [0,  1,  2]

# Input:  arr[]   = [50, 40, 70, 60, 90]
# index[] = [3,  0,  4,  1,  2]
# Output: arr[]   = [40, 60, 90, 50, 70]
# index[] = [0,  1,  2,  3,   4]
def reorder(arr, index):
    n = len(arr)
    m = len(index)
    newarr = [0] * n
    for i in range(0, n):
        newarr[index[i]] = arr[i]
    print(newarr)
    print(sorted(index))


arr = list(map(int, input("enter array").strip().split()))
index = list(map(int, input("Enter index array").strip().split()))
n = len(arr)
reorder(arr, index)
