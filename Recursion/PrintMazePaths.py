ans = 0
def sol(n, m, r, c):
    global ans
    if r == m or c == n:
        return

    if r == m - 1 and c == n - 1:
        ans += 1
        return

    sol(n, m, r + 1, c)
    sol(n, m, r, c + 1)




if __name__ == '__main__':

    n=1;
    m=5;
    sol(n,m,0,0)
    print(ans)
