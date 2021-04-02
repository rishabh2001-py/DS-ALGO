

def FindMaxdistance(arr,n):
    brr=[0]*(n*2)
    for i in range(0,2*n):
        brr[i]=arr[i%n]
    maxham=0
    for j in range(0,n):
        temp=brr[0]
        for j in range(0,n):
            brr[j]=brr[j+1]
        brr[n-1]=temp
        currsum=0
        for k in range(0,n):
            if(brr[k]!=brr[n+k]):
                currsum=currsum+1
            if(maxham==n):
                return n
            if(maxham<currsum):
                maxham=currsum
    return maxham
















arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(FindMaxdistance(arr,n))