#Given  arrays  of different sizes, find the number of distinct triplets (p,q,r)
# where p belongs to a ,q to b, r to c  written as(p,q,r) and satisfying the criteria: p<=q>=r:


def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort()
    b.sort()
    c.sort()

    count = 0

    for i in range(len(b)):
        rcount = binarySearch(c, b[i]) + 1
        lcount = binarySearch(a, b[i]) + 1

        count = count + (rcount * lcount)

    return count


def binarySearch(arr, ele):
    low = 0
    high = len(arr) - 1
    indexcount = -1

    while (low <= high):

        mid = int((low + high) // 2)

        if (arr[mid] <= ele):
            indexcount = mid
            low = mid + 1
        else:
            high = mid - 1
    return indexcount



a=list(map(int,input("Enter Array 1:").strip().split()))
b=list(map(int,input("Enter Array 2:").strip().split()))
c=list(map(int,input("Enter Array 3:").strip().split()))


count=triplets(a,b,c)
print("The distinct triplets are::",count)

