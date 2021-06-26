import numpy as np

def GoldMine(arr):

    row=len(arr)
    column=len(arr[0])

    dp= (row * column) * [0]
    dp = np.array(dp).reshape(row,column)

    for j in range(column-1,-1,-1):
        for i in range(0,row):

            if (j == column-1):
                dp[i][j] = arr[i][j]
            elif(i == 0):
                dp[i][j] = arr[i][j] + max(dp[i][j+1],dp[i+1][j+1])
            elif(i == row-1):
                dp[i][j] = arr[i][j]+ max(dp[i][j+1],dp[i-1][j+1])
            else:
                dp[i][j] = arr[i][j] + max(dp[i][j+1],dp[i+1][j+1],dp[i-1][j+1])
    print(arr,"\n")
    print(dp)
    maximum = -10**9
    for i in range(row):
        maximum = max(dp[i][0],maximum)
    print("Maximum is ",maximum)






if __name__ == '__main__':
    arr=[[1,2,90,4,5],
         [9,7,4,99,12],
         [5,1,7,1,9]]
    arr = np.array(arr).reshape(3,5)
    GoldMine(arr)
    # print(arr)
















