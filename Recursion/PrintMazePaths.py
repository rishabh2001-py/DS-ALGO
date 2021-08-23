ans = 0
def sol(n, m, r, c,psof):
    global ans
    if r == m or c == n:
        return

    if r == m - 1 and c == n - 1:
        print(psof)
        ans += 1
        return

    sol(n, m, r + 1, c,psof+"v")
    sol(n, m, r, c + 1,psof+"h")




if __name__ == '__main__':

    n=3;
    m=3;
    sol(n,m,0,0,"")
    print(ans)
