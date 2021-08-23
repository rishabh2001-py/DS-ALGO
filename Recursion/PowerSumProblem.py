import math



count = 0
def powerSum(X, N):
    recur(X, N, 1, 0, "")
    # print(count)

    return count


def recur(x, n, curr, csum, sumSofar):
    global count

    if curr > int(math.pow(x, 1 / n)) + 1 or csum > x:
        # print(curr,csum)
        return

    if csum == x:
        count += 1
        print(sumSofar)
        return

    recur(x, n, curr + 1, csum + (curr ** n), sumSofar + " " + str(curr))
    recur(x, n, curr + 1, csum, sumSofar)


if __name__ == '__main__':


    X = int(input("Enter TargetSum :"))

    N = int(input("Enter Power :"))

    result = powerSum(X, N)
    print(result)
