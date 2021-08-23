#
#
# def fun(mat,r,c,ir,ic,arr,indx):
#
#     if ir == r-1:
#
#         for i in range(ic,c):
#             arr[indx+i-ic] = mat[ir][i]
#
#         print(arr)
#         return
#
#     if ic == c - 1:
#
#         for i in range(ir, r):
#             arr[indx + i - ir] = mat[i][ic]
#
#         print(arr)
#         return
#
#     arr[indx] = mat[ir][ic]
#     fun(mat,r,c,ir+1,ic,arr,indx+1)
#     fun(mat,r,c,ir,ic+1,arr,indx+1)
#
#
#
#
#
#
# mat = [[1,2,3],[4,5,6],[4,7,3]]
# arr = [0]*(3+3-1)
# fun(mat,3,3,0,0,arr,0)


# A Dynamic Programming based Python
# program for LPS problem Returns the length
# of the longest palindromic subsequence in seq
def lps(str):
    n = len(str)

    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
    R = [[0]*n] * n
    print(L)
    print(R)
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);

    print(L)
    return L[0][n - 1]





# Driver program to test above functions
seq = "aabaa"
n = len(seq)
print("The length of the LPS is " + str(lps(seq)))
