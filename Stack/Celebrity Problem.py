def celebrity(self, M, n):
    stack = []

    for i in range(n):
        stack.append(i)

    while (len(stack) >= 2):
        c1 = stack.pop()
        c2 = stack.pop()

        if (M[c1][c2] == 0 and M[c2][c1] == 1):
            stack.append(c1)
        else:
            stack.append(c2)

    potential_celeb = stack.pop()

    for i in range(0, n):
        if (M[potential_celeb][i] != 0):
            return -1

    for i in range(0, n):
        if (M[i][potential_celeb] == 0 and i != potential_celeb):
            return -1

    return potential_celeb


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k += 1
            m.append(row)
        print(celebrity(m, n))
