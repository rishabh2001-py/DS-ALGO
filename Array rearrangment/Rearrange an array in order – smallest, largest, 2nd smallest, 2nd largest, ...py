#Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
#Output :arr[] = {1, 9, 2, 8, 3, 7, 4, 6, 5}


#Input : arr[] = [1, 2, 3, 4]
#Output :arr[] = {1, 4, 2, 3}





def rearrangeSmallestLargest(arr,n):
    s=0
    e=n-1
    arr1=sorted(arr)
    print(arr1)
    print(arr)
    i=0

    while(i<n):
        if(i%2==0):
            arr[i]=arr1[s]
            s=s+1
        else:
            arr[i]=arr1[e]
            e=e-1
        i=i+1
    return arr







    return  arr













arr = list(map(int, input("enter array").strip().split()))
n = len(arr)

print(rearrangeSmallestLargest(arr,n))