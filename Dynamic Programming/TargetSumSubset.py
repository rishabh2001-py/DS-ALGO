import numpy as np


def TargetSubsetDP(arr,target):
    row = len(arr)+1
    column = target+1
    dp = (row * column) *[0]
    dp = np.array(dp).reshape(row,column)

    for i in range(0,row):
        for j in range(0,column):

            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j == 0:
                dp[i][j] = True
            else:
                 if(dp[i-1][j] == True):
                     dp[i][j] = True
                 else:
                     val = arr[i-1]
                     # if val >= j :
                     if dp[i-1][j-val] == True:
                        dp[i][j] = True

    print(arr)
    print(dp)
    print(dp[row-1][column-1])





if __name__ == '__main__':
    arr=[1,4,5,2,1,6]
    target = 5
    TargetSubsetDP(arr,target)

