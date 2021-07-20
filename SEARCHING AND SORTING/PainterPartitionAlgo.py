
# We have to paint n boards of length {A1, A2, .. An}.
# There are k painters available and each takes 1 unit time to paint 1 unit of board.
# The problem is to find the minimum time to get this job done under the
# constraints that any painter will only paint continuous sections of boards,
# say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.
# Examples :
#
# Input : k = 2, A = {10, 10, 10, 10}
# Output : 20.
# Here we can divide the boards into 2
# equal sized partitions, so each painter
# gets 20 units of board and the total
# time taken is 20.
#
# Input : k = 2, A = {10, 20, 30, 40}
# Output : 60.
# Here we can divide first 3 boards for
# one painter and the last board for
# second painter.

######   ALGO  ######
# We also know that the values in this range
# must be in sorted order. Here our target value is the maximum sum of a
# contiguous section in the optimal allocation of boards. Now how can we apply binary search
# for this? We can fix the possible low to high range for the target value and narrow down our search to get the optimal allocation.
# We can see that the highest possible value in this range is the sum of all the elements in the
# array and this happens when we allot 1 painter all the sections of the board.
# The lowest possible value of this range is the maximum value of the array max,
# as in this allocation we can allot max to one painter and divide the other sections such that the cost of them is
# less than or equal to max and as close as possible to max. Now if we consider we use x painters in the above scenarios,
# it is obvious that as the value in the range increases, the value of x decreases and vice-versa.
# From this we can find the target value when x=k and
# use a helper function to find x, the minimum number of painters required when the maximum length of section a painter can paint is given.
#

def minTime(arr, n, k):
    low = max(arr)
    high = sum(arr)

    while (low < high):

        tempsum = 0
        mid = (low + high) // 2
        numberPainters = 1
        total = 0
        for i in range(n):
            total += arr[i]

            if (total > mid):
                total = arr[i]
                numberPainters += 1

        if (numberPainters > k):
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == '__main__':

    arr=[10,20,30,40]
    painters=2
    print("Minumum Time Required to Paint::",minTime(arr,len(arr),painters),"Minutes")


