def isSorted(arr, n, i, con):
    if n == 1:
        return True
    if con == 'Asc':
        flag = isSorted(arr[i + 1:], n - 1, i, con='Asc')
        return (arr[0] <= arr[1] and flag == True)

    if con == 'Dsc':
        flag = isSorted(arr[i + 1:], n - 1, i, con='Dsc')
        return (arr[0] >= arr[1] and flag == True)


def main():
    arr = list(map(int, input("Enter array").strip().split()))
    n = len(arr)
    print(isSorted(arr, n, 0, 'Asc'))


main()
