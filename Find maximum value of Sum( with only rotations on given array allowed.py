#Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed
#brute rule


def maximumvalueofsum(arr,n):
    maxsum=0
    maxsum1=0
    for i in range(0,n):
        temp = arr[0]
        for j in range(0,n-1):
            arr[j]=arr[j+1]
        arr[n-1]=temp
        for k in range(1,n):
            maxsum1=maxsum1+arr[k]*k
        print(maxsum1)
        if(maxsum1>maxsum):
            maxsum=maxsum1
        maxsum1=0
    return maxsum
























arr=list(map(int,input("enter array").strip().split()))
n=len(arr)
maxsum=maximumvalueofsum(arr,n)
print(maxsum)



