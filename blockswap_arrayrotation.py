                                              #REVERSE ALGO#



# Function to reverse arr[] from index start to end

def reversearray(arr,start,end):


    while (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
    print("after reversal::",arr)
    return arr

# Function to left rotate arr[] of size n by d

arr=list(map(int,input("enter array::").strip().split()))
d=int(input("Enter the d::"))
n=len(arr)
d=d%n
arr=reversearray(arr,0,d-1)
arr=reversearray(arr,d,n-1)
arr=reversearray(arr,0,n-1)
print("final rotated array::",arr)




