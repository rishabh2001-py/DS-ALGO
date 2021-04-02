import sys
def largestthree(arr,n):
    max1=max2=max3=-sys.maxsize
    for i in range(0,n):
        if(arr[i]>max1):
            max3=max2
            max2=max1
            max1=arr[i]
        elif(arr[i]>max2):
            max3=max2
            max2=arr[i]
        elif(arr[i]>max3):
            max3=arr[i]
    return max1,max2,max3
























arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(largestthree(arr,n))