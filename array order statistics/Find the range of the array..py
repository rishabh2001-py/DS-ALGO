#0(n)
import sys


def RangeOfArray(arr, n):
    ranger = 0
    minimum = sys.maxsize
    maximum = -sys.maxsize
    for i in range(0,n):
        if (arr[i] > maximum):
            maximum = arr[i]
        if (arr[i] < minimum):
            minimum = arr[i]
    ranger = abs(maximum - minimum)
    return ranger


arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(RangeOfArray(arr,n))
