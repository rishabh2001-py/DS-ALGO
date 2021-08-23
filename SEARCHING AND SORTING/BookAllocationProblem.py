# a = [10,20,15,5,10]
# m = 3

def bookAlocation(arr,m):

    low = max(arr)
    high = sum(arr)
    mid = 0
    while(low<=high):
        mid = (low+high)//2
        # print("Mid :",mid)
        if(possible(arr,m,mid)):
            low = mid + 1
        else:
            high = mid - 1

    return low

def possible(arr,m,mid):

    PossibleStudent = 1
    sum=0
    for i in range(len(arr)):
        if(sum>mid):
            sum = 0
            PossibleStudent+=1
        else:
            sum += arr[i]

    return PossibleStudent >= m




if __name__ == '__main__':
    # arr = [int(i) for i in input("Enter the Pages of Books : ").split()]
    # m = int(input("Number Of students : "))
    arr =[30,23,76,90]
    m = 2

    print(bookAlocation(arr,m))























