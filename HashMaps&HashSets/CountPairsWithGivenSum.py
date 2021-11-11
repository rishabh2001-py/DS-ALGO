def getPairsCount(arr, n, k):
    m = {}
    for i in arr:
        try:
            m[i] += 1
        except:
            m[i] = 1

    count = 0
    for i in range(n):

        try:
            count += m[k - arr[i]]

            if k - arr[i] == arr[i]:
                count -= 1
        except:
            pass

    return count // 2


if __name__ == '__main__':

    arr = [2,3,5,7,1,1]

    res = getPairsCount(arr,8,len(arr))
    print(res)










