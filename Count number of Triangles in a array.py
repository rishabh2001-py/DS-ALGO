def Count(arr,n):
    arr.sort()
    count=0
    for i in range(0,n-2):

        k=i+2
        for j in range(i+1,n-1):
            while(k<n and arr[i]+arr[j]>arr[k]):
                k+=1
                count += k-j-1

    return count




if __name__ == '__main__':
    arr=[26,9,27,22,16,27]
    print(Count(arr, len(arr)))



