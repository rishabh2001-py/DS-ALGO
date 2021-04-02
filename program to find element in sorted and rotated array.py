def binarysearch(arr,n,low,high,key):
    while(high>=low):
        mid=((low+high)//2)
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            low=mid+1
        elif(arr[mid]>key):
            high=mid-1
    return -1
def mainpivotedfunc(arr,n,key):
    high=n-1
    low=0
    mid=high+low//2
    if(arr[mid]==key):
        return mid
    pivot=FindPivotedIndex(arr,n,low,high)
    print("pivoted element at index %d"%pivot)
    if(pivot==-1):
        return binarysearch(arr,n,low,high)
    elif(arr[pivot]==key):
        return pivot
    elif(arr[0]<=key):
        return binarysearch(arr,n,low,pivot-1,key)
    else:
        return binarysearch(arr,n,pivot+1,high,key)



def FindPivotedIndex(arr,n,low,high):
    if(high<low):
        return -1
    if(high==low):#base case if list is of single element
        return low

    mid=low+high//2
    if(arr[mid]>arr[mid+1]) : #case, if middle index value is greater than next index value then the next index should be pivoted
        return mid+1
    elif(arr[low]>arr[mid]): # case,if the starting index is less than than middle ,then pivot must lie in first half
        return FindPivotedIndex(arr,n,low,mid-1)
    else:
        return FindPivotedIndex(arr,n,mid+1,high) # case,if the starting index is smaller than middle,then pivot must lie in 2nd half



arr=list(map(int,input("enter array").strip().split()))
key=int(input("enter key"))
n=len(arr)
flag=mainpivotedfunc(arr,n,key)
if(flag==-1):
    print("ELEMENT NOT FOUND")
else:
    print("Element found at %d"%flag)

