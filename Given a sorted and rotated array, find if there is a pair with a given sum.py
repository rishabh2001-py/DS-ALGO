def PairSum(arr, Sum, n):
    for i in range(0, n - 1):
        if (arr[i] > arr[i + 1]):
            break;
    minele = i + 1
    maxele = i
    print(minele)
    print(maxele)
    count = 0
    while (minele != maxele):
        if (arr[minele] + arr[maxele] == Sum):
            count = count + 1
        if (arr[minele] + arr[maxele] > Sum):
            maxele = (n + maxele - 1) % n
        else:
            minele = (minele + 1) % n
    return count


arr = list(map(int, input("enter array").strip().split()))
Sum = int(input("enter Sum"))
n = len(arr)
result = PairSum(arr, Sum, n)
if (result == 0):
    print("Pair not found")
else:
    print("Pair found ", result, "times")
