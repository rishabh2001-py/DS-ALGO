def maxLenIS(arr, n):

    dp = [0] * (n)
    dp[0] = 1
    for i in range(n):
        currmax = 1
        for j in range(i):

            if arr[i] > arr[j]:
                currmax = max(dp[j],currmax) + 1

        dp[i] = currmax

    return max(dp)


if __name__ == '__main__':

    arr = [1,101,3,4,100]

    print(maxLenIS(arr,len(arr)))