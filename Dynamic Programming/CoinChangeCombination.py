
def CoinChangeCombination(coins,amount):

     dp=[0]*(amount+1)

     dp[0]=1
     for i in range(len(coins)):
         for j in range(coins[i],len(dp)):
             dp[j]+=dp[j-coins[i]]

     print("Number of ways :",dp[amount])
     # print(dp)





if __name__ == '__main__':

    # coins = list(map(int,input().strip().split()))
    coins=[10,20,50]
    amount=int(input("Enter amount: "))
    CoinChangeCombination(coins,amount)


