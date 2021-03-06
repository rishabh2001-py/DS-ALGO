def maxSumIS(arr, n):
    
    dp = [0] * (n)
    dp[0] = arr[0]
    for i in range(n):
        currmax = arr[i]
        for j in range(i):

            if arr[i] > arr[j]:
                currmax = max(arr[i] + dp[j], currmax)

        dp[i] = currmax

    return max(dp)


if __name__ == '__main__':
    arr = [11,22,44,6,1,4,89]
    print(maxSumIS(arr, len(arr)))
