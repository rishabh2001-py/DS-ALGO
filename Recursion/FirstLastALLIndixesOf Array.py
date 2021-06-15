def FirstOcurence(arr, key, n, i):
    if n == i:
        return -1

    if (arr[i] == key):
        return i

    return (FirstOcurence(arr, key, n, i + 1))


def LastOcurenec(arr, key, n, i):
    if i == n:
        return -1

    restarray = LastOcurenec(arr, key, n, i + 1)

    if (restarray != -1):
        return restarray
    if arr[i] == key:
        return i
    return -1
def allIndices(arr,key,n,i):
    if n == i:
        a=list()
        return a
    a=allIndices(arr,key,n,i+1)
    if(arr[i]==key):
        a.append(i)
    return a



def main():
    # arr = list(map(int, input("Enter array").strip().split()))
    arr = [1,1,2,2,2,2,1,1,5,6,8,9]
    n = len(arr)
    key = int(input("Enter Key:"))
    print("First Ocurence:",FirstOcurence(arr, key, n, 0))
    print("Last Ocuurence:",LastOcurenec(arr, key, n, 0))
    print(allIndices(arr,key,n,0))


main()
