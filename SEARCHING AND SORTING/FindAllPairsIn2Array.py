def allPairs(A, B, N, M, X):
    ans = []

    A.sort()
    B = sorted(B, reverse=True)
    i = 0
    j = 0
    while (i < N and j < M):
        if (A[i] + B[j] < X):
            i += 1
        elif (A[i] + B[j] > X):
            j += 1
        else:
            ans.append([A[i], B[j]])
            i+=1
            j+=1

    print(ans)


if __name__ == '__main__':
    A=[1,2,4,5,7]
    B=[5,6,3,4,8]
    X= 9
    allPairs(A,B,5,5,X)