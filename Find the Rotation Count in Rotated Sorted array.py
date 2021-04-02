def countroatatednumber(arr,n):
    count=0;

    for i in range(0,n-1):
        if(arr[i]>arr[i+1]):
            count=i+1
    return count







arr=[7,8,9,3,4,5]
n=len(arr)
print(countroatatednumber(arr,n))