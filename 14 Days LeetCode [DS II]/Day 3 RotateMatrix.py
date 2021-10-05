def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[(n - 1) - i][j] = matrix[(n - 1) - i][j], matrix[i][j]

    # print(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



m1 =[[1,2,3],[4,5,6],[7,8,9]]
m2 =[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
m3 =[[1]]
m4 =[[1,2],[3,4]]
rotate(m2)
print(m2)