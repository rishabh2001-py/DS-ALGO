# A[i] >= A[i - 1]

# if i is even.

# A[i] <= A[i - 1] if i is odd


def rearrangeArray(arr, n):
    for i in range(1, n, 2):
        if (arr[i] >= arr[i - 1]):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr

arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(rearrangeArray(arr,n))
