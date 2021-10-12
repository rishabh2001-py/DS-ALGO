longest = 0
# def bruteLongestSubstring(s,res,pos):
#     global longest
#     if len(s) == pos:
#         print(res)
#         if(isPalindrome(res)):
#             if len(res) > longest:
#                 longest = len(res)
#
#         return
#
#     for i in range(len(s)):
#         bruteLongestSubstring(s[pos],res+s[pos],pos+1)
#
#

def isPalindrome(s):
    # print(s)
    start = 0
    end = len(s)-1

    while(end>=start):

        if s[end] != s[start]:
            return False
        start+=1
        end-=1

    return True






def main():
    global longest
    s = "aabc"

    # (bruteLongestSubstring(s,"",0))
    print(longest)


main()