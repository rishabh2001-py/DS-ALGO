# O(N)


def maxPROFIT(arr, n):
    profit = -100000000
    currprofit = 0
    minsofar = arr[0]
    for i in range(0, n):
        currprofit = arr[i] - minsofar  # taking first element as minsofar
        if (arr[i] < minsofar):  # keeps on checking minsofar ,if arr[i] is less than minsofar
            minsofar = arr[i]  # minsofar=arr[i]
        profit = max(profit, currprofit)
    print("Profit is", profit, "Rupees.")


arr = [5, 1, 2, 3, 7, 9, 1, 3, 5, 0, 1]
n = len(arr)
maxPROFIT(arr, n)
