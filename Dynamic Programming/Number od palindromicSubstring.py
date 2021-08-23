

# [ 1 1 1 1 ]
# [ 0 1 1 1 ]
# [ 0 0 1 1 ]
# [ 0 0 0 1 ]


def CountPalin(s,n):
    
    dp = [[True]*n]*n
    count = 0
    for gap in range(n):
        i = 0
        j = gap
        while(i<n-gap and j<n):

            if gap == 0 :
                dp[i][j] = True

            elif gap == 1:
                if(s[i] == s[j]):
                    dp[i][j] = True
                    print(s[i:j+1])
                    count+=1
            else:
                if(s[i] == s[j] and dp[i-1][j-1] == True):
                    dp[i][j] = True
                    print(s[i:j+1])
                    count+=1
            i+=1
            j+=1

    print(count)




CountPalin('abaa',5)
























