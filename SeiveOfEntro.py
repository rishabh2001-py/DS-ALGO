def sieveOfEratosthenes(N):
    arr = [0] * (N + 2)

    for i in range(2, N + 1):
        if arr[i] == 0 :
            j = i * i
        while (j < N + 1):
            arr[j] = 1
            j = j + i

    res = []

    for i in range(2, N + 1):
        if arr[i] == 0:
            res.append(i)

    return res


if __name__ == '__main__':
    n = int(input("Enter The Range :"))
    print(sieveOfEratosthenes(n))