def threeSum(nums):
    nums.sort()
    n = len(nums)
    S = set()
    l = list()

    for i in range(0, n):
        s = i + 1
        e = n - 1

        while (s < e):

            sum0 = nums[i] + nums[s] + nums[e]

            if (sum0 > 0):
                e = e - 1
            elif (sum0 < 0):
                s = s + 1
            else:
                S.add((nums[i], nums[s], nums[e]))
                s, e = s + 1, e - 1

    return ((S))


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))

    print(threeSum(arr))