


import numpy as np
def FindPalindromicnumber(s):

    dp_arr= len(s)**2 * [0]
    dp_arr = np.array(dp_arr).reshape(len(s),len(s))
    count=0
    max_length=0
    longest_subs=""
    for i in range(len(s)):
        row = 0
        column = i
        for j in range(column,len(dp_arr)):
            if(i == 0):
                dp_arr[row][column]= 1
                max_length = 1
                longest_subs=s[row:column]

            elif(i == 1):
                if(s[row] == s[column]):
                    dp_arr[row][column] = 1
                    max_length = 2
                    longest_subs = s[row:column]
            elif(i>1):
                if(s[row] ==  s[column] and dp_arr[row+1][column-1] == 1 ):
                    dp_arr[row][column] = 1
                    if len(s[row:column])+1 > max_length:
                        max_length = len(s[row:column])+1
                        longest_subs = s[row:column+1]
                else:
                    dp_arr[row][column] = 0
            if (dp_arr[row ][column ] == 1):
                count += 1

            row += 1
            column += 1


    print(dp_arr)
    print("Number Of Palindromic substring:",count)
    print("Longest Palindromic Subs:",longest_subs)
    print("max_length",max_length)









if __name__=='__main__':
    s=input("Enter String::")
    FindPalindromicnumber(s)
