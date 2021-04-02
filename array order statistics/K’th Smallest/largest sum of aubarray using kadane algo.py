# KADANE'S ALGO
# The simple idea of Kadane’s algorithm is to look for
# all positive contiguous segments of the array (max_ending_here is used for this).
# And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this).
# Each time we get a positive-sum compare it with max_so_far and
# update max_so_far if it is greater than max_so_far

import sys


def maxsumkadane(arr, n):
    currsum = 0
    maxsum = -sys.maxsize
    for i in range(0, n):
        currsum = currsum + arr[i]
        if (currsum > maxsum):
            maxsum = currsum
        if (currsum < 0):
            currsum = 0
    print(maxsum)


arr = list(map(int, input("Enter array").strip().split()))
n = len(arr)
maxsumkadane(arr, n)
