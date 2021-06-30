

def eqb(A,N):
    totalsum = sum(A)

    prevsum = 0
    nextsum = totalsum
    ans = -1
    for i in range(0, N):
        print(prevsum,nextsum)
        if prevsum == nextsum-A[i]:
            ans = i
            break;
        prevsum += A[i]
        nextsum -= A[i]

    print(ans + 1)

if __name__ == '__main__':
    arr=[1,3,2,5,2,2,2]
    eqb(arr,len(arr))



