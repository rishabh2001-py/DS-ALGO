def minDist(arr, n, x, y):
    import sys

    def minDist(arr, n, x, y):

        # previous index and min distance
        i = 0
        p = -1
        min_dist = sys.maxsize;

        for i in range(n):

            if (arr[i] == x or arr[i] == y):

                # we will check if p is not equal to -1 and
                # If the element at current index matches with
                # the element at index p , If yes then update
                # the minimum distance if needed
                if (p != -1 and arr[i] != arr[p]):
                    min_dist = min(min_dist, i - p)

                p = i

        if (min_dist == sys.maxsize):
            return -1
        return min_dist

    # arr = list(map(int, input("enter array").strip().split()))


arr = [13, 98 ,5 ,10 ,23, 13,4, 53, 60, 78, 66, 68, 44, 69, 79, 71, 90, 17, 91 ,84, 34, 52 ,12 ,11 ,57 ,61, 2]
n = len(arr)
x, y = map(int, input("Enter X and Y").strip().split())
print(minDist(arr, n, x, y))
