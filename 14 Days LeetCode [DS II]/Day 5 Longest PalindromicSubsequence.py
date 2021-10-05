def longestPalindrome(s):
    m = {}
    for i in s:
        try:
            m[i] += 1
        except:
            m[i] = 1

    ans = 0
    for i in m:

        ans += m[i] // 2 * 2

        if ans % 2 == 0 and m[i] % 2 == 1:
            ans += 1

    return ans

if __name__ == '__main__':

    s = "banans"
    ans = longestPalindrome(s)
    print("Longest Palnidrome is of length :",ans)