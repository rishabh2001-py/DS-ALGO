def kthElement( arr1, arr2, n, m):
    arr = []
    i = 0
    j = 0
    while (n > 0 and m > 0):
        if (arr1[i] > arr2[j]):
            arr.append(arr2[j])
            j+=1
            m -= 1
        elif (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i += 1
            n-= 1
        else:
            arr.append(arr1[i])
            i += 1
            j+=1
            m-=1
            n-=1
    while (n > 0):
        arr.append(arr1[i])
        n-= 1
        i+=1
    while (m > 0):
        arr.append(arr2[j])
        m-=1
        j+=1
    print(arr)

arr1 = list(map(int, input("enter array").strip().split()))
n = len(arr1)
arr2 = list(map(int, input("enter array").strip().split()))
m= len(arr2)
kthElement(arr1,arr2,n,m)
