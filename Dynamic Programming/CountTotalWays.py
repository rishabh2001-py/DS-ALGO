
# Given N, the number of plots on either sides of the road.
# Find the total ways to construct buildings in the plots such that there is a space between any 2 buildings.
# All plots on one side of the road are continuous.
# Lets suppose ‘*’ represents a plot, then for N=3, the plots can be represented as * * * | | * * *
# Where | | represents the road.
#
# Input: N = 3
# Output: 25
# Explanation: 3 plots, which means possible
# ways for one side are BSS, BSB, SSS, SBS,
# SSB where B represents a building and S
# represents an empty space Total possible
# ways are 25, because a way to place on one
# side can correspond to any of 5 ways on other
# side.


def TotalWays(N):

    countPlot = 1
    countSpace = 1

    for i in range(2 , N+1):

        temp = countSpace
        countSpace = countSpace+ countPlot
        countPlot = temp

    return ((countSpace +countPlot )**2) % 1000000007

if __name__ == '__main__':

    n = int(input("Enter N: "))
    print(TotalWays(n))