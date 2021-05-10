def minimumSwaps(arr):
    arr2 = []
    for i in range(len(arr)):
        arr2.append([arr[i], i])
    arr2.sort()
    count = 0
    print(arr2)

    j = 0
    while (j <= len(arr)):
        pass
        if (j != arr2[j][1]):
            while (j != arr2[j][1]):
                print(j,arr2[j][1])
                count += 1
                arr2[j], arr2[arr2[j][1]] = arr2[arr2[j][1]],arr2[j]
        j = j + 1

    return count


arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(minimumSwaps(arr))