def lengthOfLongestSubstring(s):
    i = -1
    j = -1
    s1=""
    ans = 0

    m = {}

    while (True):
        flag1 = False
        flag2 = False

        while (j < len(s) - 1):
            flag1 = True
            j += 1
            try:
                m[s[j]] += 1
            except:
                m[s[j]] = 1

            if (m[s[j]] == 2):
                break;
            else:
                #s1=s1+s[j]
                curr=j-i
                if (curr > ans):
                    ans = curr
# Release
        while (i < j):

            flag2 = True
            i += 1
            m[s[i]] -= 1
            s1=list(s1)
#           s1.pop(i)

            if (m[s[i]] == 1):
                #s1=str(s1)
                #s1.join("")
                break

        if (flag1 == False and flag2 == False):
            break;
    #print(s1)
    return ans


def main():

    s=input("Enter String: ")
    print(lengthOfLongestSubstring(s))

main()














