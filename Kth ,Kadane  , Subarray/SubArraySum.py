def subArraySum(arr, n, s):
    start = 0
    i = 0
    currsum = 0

    while (i < len(arr)):
        if currsum < s:
            currsum += arr[i]
            i += 1
        if (currsum > s):
            currsum -= arr[start]
            start += 1
        if currsum == s:
            return [start + 1, i]

    for j in range(n):
        if (arr[j] == s):
            return [j + 1, j + 1]

    return [-1,-1]



if __name__ == '__main__':

    arr=list(map(int,input("Enter Array::").strip().split()))
    sum=int(input("Enter the sum::"))
    print(subArraySum(arr,len(arr),sum))
    # print(arr[ls[0]-1:ls[1]])

