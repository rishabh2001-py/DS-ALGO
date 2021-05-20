# Given an array and a number k where k is smaller than size of array,
# we need to find the k’th smallest element
# in the given array. It is given that all array elements are distinct.
# example#
# Input: arr[] = {7, 10, 4, 3, 20, 15}
# k = 3
# Output: 7

# Input: arr[] = {7, 10, 4, 3, 20, 15}
# k = 4
# Output: 10

import heapq


def kthSmallest(arr, k):
    if k > len(arr) or k <= 0:
        print('INDEX OUT OF RANGE')
        return
    heapq.heapify(arr)
    count = 0
    while (k != count):
        x = heapq.heappop(arr)
        count += 1
    print(x)


k = int(input("Enter K: "))
arr = list(map(int, input("ENTER ARRAY : ").strip().split()))

kthSmallest(arr, k)
