
def findTwoElement(arr, n):
    a = [0] * 2
    k = list(set(arr))
    a[0] = sum(arr) - sum(k)
    a[1] = ((n * (n + 1) // 2)) - sum(k)

    print(a)


if __name__ == '__main__':

    arr= list(map(int,input("Enter Array").strip().split()))
    n=len(arr)
    findTwoElement(arr,n)