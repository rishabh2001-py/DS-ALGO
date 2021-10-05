# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#Input: nums = [4,1,2,1,2]
# Output: 4
# You must implement a solution with a linear runtime complexity and use only constant extra space.




def singleNumber(nums):
    res = 0

    for i in range(len(nums)):
        res ^= nums[i]

    return (res)


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))

    print(singleNumber(arr))