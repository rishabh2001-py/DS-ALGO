def DispalyArray(arr, n):
    if (n == 0):
        return
    DispalyArray(arr, n - 1)
    print(arr[n-1],end=" ")


def MaximumOfArray(arr,indx):
    if(indx==len(arr)-1):
        return arr[indx]
    maximum=MaximumOfArray(arr,indx+1)
    maximum=max(arr[indx],maximum)
    return maximum




if __name__ == '__main__':
    arr = [1,4,998.89898,99,3,90]
    (DispalyArray(arr, len(arr)))
    print()
    print("Maximum is:",MaximumOfArray(arr,0))
