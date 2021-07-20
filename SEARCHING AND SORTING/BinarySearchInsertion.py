
def BinarySearchInsertion(arr,target):

    high = len(arr)-1
    low = 0

    while(low<high):
        mid = (low+high)//2
        print(low,mid,high)
        if(target<arr[mid]):
            high = mid - 1
        elif(target > arr[mid]):
            low =mid + 1
        else:
            print(mid)
            break
    if target > arr[high]:
        print(high+1)
    elif  target < arr[low]:
        print(low)






if __name__ == '__main__':
    arr=[1,3]
    BinarySearchInsertion(arr,3)














