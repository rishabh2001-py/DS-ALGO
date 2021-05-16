# The staircase has 5 steps. it can take sequences of steps:

# steps=[1 1 1 1 1
#  1 1 1 2
# 1 1 2 1
# 1 2 1 1
# 2 1 1 1
# 1 2 2
# 2 2 1
# 2 1 2
# 1 1 3
# 1 3 1
# 3 1 1
# 2 3
# 3 2]


def stepPerms(n):
    if n == 1 or n == 2:
        return n
    if (n == 3):
        return 4
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n - 1]


def main():
    n = int(input("Enter number of Steps::"))

    print(stepPerms(n))


main()
