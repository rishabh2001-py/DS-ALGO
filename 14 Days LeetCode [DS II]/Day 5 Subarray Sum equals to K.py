



def subarraySum(nums,k):
    if len(nums) == 1:
        if k == nums[0]:
            return 1
        else:
            return 0

    s = {0: 1}
    count = 0
    sm = 0
    for i in range(len(nums)):
        sm += nums[i]
        if sm - k in s:
            count += s[sm - k]

        if sm in s:
            s[sm] += 1
        else:
            s[sm] = 1

    return count


if __name__ == '__main__':

    arr = list(map(int,input().strip().split()))
    k = int(input())
    print(subarraySum(arr,k))








