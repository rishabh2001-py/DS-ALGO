import sys

def maxSUM(arr,n):
    maxsum=-sys.maxsize
    sumarr=[0]*n
    sumarr[0]=arr[0]
    currsum=0
    l=0
    r=0
    for i in range(1,n):
        sumarr[i]=arr[i]+sumarr[i-1]
    print(sumarr)
    i=0
    for i in range(0,n):
        for j in range(i,n):
            currsum=sumarr[j]-sumarr[i]+arr[i]
            if (currsum>maxsum):
                maxsum=currsum
                l=i
                r=j
    print(maxsum,"starting index",l,"end index",r)




















arr=list(map(int,input("Enter array").strip().split()))
n=len(arr)
maxSUM(arr,n)
#{-2, -3, 4, -1, -2, 1, 5, -3}