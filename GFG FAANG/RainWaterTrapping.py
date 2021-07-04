
def trapFunction(arr,n):

    right = [0]*n
    left = [0]*n

    left[0]=arr[0]
    maxi = left[0]
    for i in range(1,n):
        maxi = max(maxi,arr[i])
        left[i] = maxi;

    right[n-1] = arr[n-1]
    maxi = right[n-1]
    for i in range(n-2,-1,-1):
        maxi = max(arr[i],maxi)
        right[i] = maxi

    result = 0
    for i in range(n):
        result+=min(left[i],right[i])-arr[i]


    print(result)


if __name__ == '__main__':
    arr=[3,1,2,4,0,1,3,2]
    trapFunction(arr,len(arr))