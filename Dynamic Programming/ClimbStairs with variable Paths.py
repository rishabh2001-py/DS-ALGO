 

#dp tabulation method
def stairspath(arr,n):

    dp = (n+1) * [0]
    dp[n] = 1

    for i in range(n-1,-1,-1):
        j=1
        while(j<=arr[i] and j+i < len(dp)):
            dp[i] += dp[i + j]
            j+=1

    print(dp[0])

if __name__ == '__main__':

    arr= [3,3,0,2,2,3]
    stairspath(arr,len(arr))
