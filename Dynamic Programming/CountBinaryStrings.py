


def countBinary(n):

    count0 = 1
    count1 = 1

    for i in range(2, n + 1):
        temp = count0
        count0 = count1 + count0
        count1 = temp

    return (count0 + count1) % (10 ** 9 + 7)


if __name__ == '__main__':

    n = int(input("Enter N: "))
    print(countBinary(n))
