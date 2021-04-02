#program to rotate array cyclically





def rotateClockwise(arr,n,d):
    for i in range(0,d):
        temp=arr[n-1]
        for j in range(n-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=temp

    return arr

arr=list(map(int,input("enter array:: ").strip().split()))
d=int(input("enter the d:"))
n=len(arr)

arr=rotateClockwise(arr,n,d)
print(arr)



