def binarysearch(arr,n,key):
    low=0
    high=n-1
    while(high>low):
        mid=(low+high//2)
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            low=mid+1
        elif(arr[mid]>key):
            high=mid-1
    return -1

if __name__ == '__main__':
    arr=list(map(int,input("enter array").strip().split()))
    key=int(input("enter key"))
    n=len(arr)
    flag=binarysearch(arr,n,key)
    if(flag==-1):
       print("ELEMENT NOT FOUND")
    else:
       print("Element found at %d"%flag)
