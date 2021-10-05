def getRow(n):
    dp = []
    dp.append([1])
    dp.append([1, 1])
    for i in range(2, n + 1):
        # print(dp)
        arr = []
        for j in range(i + 1):
            if j == 0 or j == i:
                arr.append(1)
            else:
                arr.append(dp[i - 1][j - 1] + dp[i - 1][j])

        dp.append(arr)

    return (dp[n])


def main():
    print(getRow(4))

main()
