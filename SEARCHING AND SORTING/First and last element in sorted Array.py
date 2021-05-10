def binarysearch(arr,s,e,key):
    n=len(arr)
    low=0
    high=n-1

    while(high>low):
        mid=(low+high//2)
        if(arr[mid]==key and arr[mid]):
            return mid
        elif(arr[mid]<key):
            low=mid+1
        elif(arr[mid]>key):
            high=mid-1
    return -1

def searchRange(nums, target):


    n=len(nums)
    s= binarysearch(nums,0,n-1,target)
    e=binarysearch(nums,0,n-1,target)

    return [s,e]

















nums = list(map(int, input("Enter Array:").strip().split()))
target=int(input('Target:'))
print(searchRange(nums,target))