# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

#  Example :
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.



def rob(nums):

    n = len(nums)
    dp = [0] * n

    dp[ n -1] = nums[ n -1]
    dp[ n -2] = nums[ n -2]

    ma = dp[ n -1]

    for i in range( n -3 ,-1 ,-1):

        dp[i] = nums[i] + ma

        ma = max(dp[ i +1] ,ma)

    return max(dp[0] ,ma)


if __name__ == "__main__":
    arr = [2,7,9,3,1]
    print(rob(arr))







