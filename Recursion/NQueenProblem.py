

def Nqueen(chess,row,psof):

    if row == len(chess):
        print(psof)
        return


    for col in range(len(chess)):

        if  IsSafe(chess,row,col):
            chess[row][col] = 1
            Nqueen(chess,row+1,psof + str(row)+str(col)+'-')
            chess[row][col] = 0



def IsSafe(chess,row,col):

    for i in range(row-1,-1,-1):
        print(i,col)
        if(chess[i][col]==1):
            return False

    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if chess[i][j] == True:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, len(chess[0]))):
        if chess[i][j] == False:
            return False

    return True






if __name__ == '__main__':
    n = int(input("Enter the N :"))
    chess = [[0]*n] * (n*n)

    Nqueen(chess,0,"")

