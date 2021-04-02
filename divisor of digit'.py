def findDigits(n):
    num = 0
    count = 0
    while (n >= 1):
        num = n % 10
        if (num != 0 and n % num == 0):
            count = count + 1
        n = n // 10
    print(count)


l1 = [11, 123456789, 114108089, 110110015, 121, 33, 44, 55, 66, 77, 88, 106108048]
for i in range(0, len(l1)):
    findDigits(l1[i])
