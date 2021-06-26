
# dp tabulation method
def stairspath(arr ,n):

    dp = (n+1) * [None]

    dp[n] = 0


    for i in range( n-1 ,-1 ,-1):
        if arr[i] != 0:
            j=1
            mini=10**9
            while (j<=arr[i] and j+i < len(dp)):
                if (dp[i+j] != None ):
                    mini = min(dp[i+j],mini)
                j+=1
            if mini != 10 ** 9 :
                dp[i] = mini + 1
    print(dp[0])





if __name__ == '__main__':

    arr= [1,2,2,1,5,9]
    stairspath(arr,len(arr))
