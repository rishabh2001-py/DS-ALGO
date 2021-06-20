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
    dp= (n) * [0]

    for i in range(n):
        if i==0:
            dp[0]=1
        elif i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i-1] + dp [i-2] + dp [i-3]

    print(dp[n-1])


def main():
    n = int(input("Enter number of Steps::"))

    stepPerms(n)


main()
