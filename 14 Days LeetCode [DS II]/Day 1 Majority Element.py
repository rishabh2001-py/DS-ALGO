def majorityElement(nums):
    m = {}

    for i in range(len(nums)):

        try:
            m[nums[i]] += 1
        except:
            m[nums[i]] = 1

    for i in m:
        if m[i] > (len(nums) // 2):
            return i


if __name__ == '__main__':
    
    arr = list(map(int,input().strip().split()))

    print(majorityElement(arr))