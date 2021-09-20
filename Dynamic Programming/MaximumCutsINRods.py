def maximizeTheCuts(arr,n):
    dp = [-1] * (n + 1)
    dp[0] = 0


    for i in range(1, n + 1):
        curmax = -1
        for j in range(3):
            if arr[j] <= i and dp[i - arr[j]] != -1:
                curmax = max(dp[i - arr[j]] + 1, curmax)

        dp[i] = curmax

    if dp[n] == -1:
        return 0
    return dp[n]



if __name__ == '__main__':

    arr = [2,3,4]
    n = 6
    ans = maximizeTheCuts(arr,n)

    print(ans)






