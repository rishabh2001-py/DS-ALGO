def nextPermutation(arr,n):
    idx = -1;
    for i in range(n - 1, 0, -1):
        if (arr[i - 1] < arr[i]):
            idx = i
            break;
    # print(arr[idx])
    if (idx == -1):
        arr.reverse()
        return arr

    temp = idx
    for i in range(idx + 1, n):
        if (arr[idx - 1] < arr[i] and arr[temp] > arr[i]):
            temp = i

    arr[temp], arr[idx - 1] = arr[idx - 1], arr[temp]

    low = idx
    high = n - 1

    while (low < high):
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

    print(arr)

if __name__ == '__main__':
    n=int(input("Enter Number"))
    list=list(map(int,input().strip().split()))
    nextPermutation(list,n)




