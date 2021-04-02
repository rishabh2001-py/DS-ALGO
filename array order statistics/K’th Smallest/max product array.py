


def maxproduct(arr, n):
    maxprod = arr[0]
    maxprodarray = [arr[0]]
    minprod = arr[0]
    temp1 = 1
    tempmin = 1

    for i in range(1, n):
        if (arr[i] == 0):
            temp1 = 1
            tempmin = 1
        else:
            temp1 = arr[i] * temp1
            tempmin = arr[i] * tempmin
        maxprodarray.append(max(arr[i], temp1))
        minprod = min(arr[i], tempmin)
    print((maxprodarray))
    print(max(maxprodarray))


arr = list(map(int, input("Enter array").strip().split()))
n = len(arr)
maxproduct(arr,n)

