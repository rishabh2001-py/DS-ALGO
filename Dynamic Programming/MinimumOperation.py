# Given a number N. Find the minimum number of operations required to reach N starting from 0.
# You have 2 operations available:
# Double the number
# Add one to the number


def minOperation(n):
    dp = (n + 1) * [0]

    dp[n] = 0

    for i in range(n - 1, -1, -1):
        if i * 2 <= n and i != 0:
            m = min(dp[i * 2], dp[i + 1])
            dp[i] = m + 1
        else:
            dp[i] = 1 + dp[i + 1]

    # print(dp)
    return dp[0]


if __name__=='__main__':
    print(minOperation(5))
