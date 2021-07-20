def count(S, m, target):
    dp = (target + 1) * [0]
    dp[0] = 1

    for i in range(1, target + 1):
        for j in range(m):
            if (S[j] <= i):
                dp[i] += dp[i - S[j]]

    print(dp)
    # if(dp[target]==0):
    #     return 1;
    return dp[target]
    # code here