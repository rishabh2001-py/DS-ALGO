import heapq


def minProduct(a, n, k):
    heapq.heapify(arr)
    print(arr)
    count = 0
    res = 1
    while (arr and count < k):
        x = heapq.heappop(arr)
        res = x * res
        count = count + 1
    return res


arr = [168, 372, 141, 96, 439, 187, 144, 42, 425, 286, 272, 87, 421, 311, 49, 341, 282, 255, 52, 363, 425, 350]
k = 8
n = len(arr)

print(minProduct(arr, n, k))
a = sorted(arr)
print(a)
print(n)
