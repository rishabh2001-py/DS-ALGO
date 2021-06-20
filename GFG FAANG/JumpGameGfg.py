def canReach( A, N):
    currPos = 1
    i = 0
    while (i < N):
        if  currPos + A[i] >= N:
            return 1
        else:
            currPos += A[i]
        print(currPos)
        i = currPos-1
        if A[i] == 0:
            return 0

    return 0


if __name__ == '__main__':
    arr=[2,0,3,3,3,3,0,0]

    print(canReach(arr,len(arr)))
