def fun(arr, k):
    for i in range(1, k + 1):
        start = 0
        end = len(arr)
        while (start < end):
            start += i
            end -= i
        if start == end:
            return "YES"

    return "NO"


if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(fun(arr, k))