import numpy as np

def Floodfill(maze,Row,column,pathSofar,node_visited):

    if( Row < 0 or column < 0 or Row==len(maze) or column==len(maze[0]) or maze[Row][column] == 1 or node_visited[Row][column]==True):
        return

    if(Row == len(maze)-1 and column == len(maze[0])-1 ):

        print(pathSofar)
        return
    
    node_visited[Row][column] = True

    Floodfill(maze, Row - 1, column, pathSofar + 't', node_visited)
    Floodfill(maze, Row, column - 1, pathSofar + 'l', node_visited)
    Floodfill(maze, Row + 1, column, pathSofar + 'd', node_visited)
    Floodfill(maze, Row, column + 1, pathSofar + 'r', node_visited)

    node_visited[Row][column] = False
    




if __name__ == '__main__':
    
    n,m=map(int,input("Enter Row and columns::").split())
    arr=[]
    print("Enter entries:")
    for i in range(n):
        entries=(map(int,input().split()))
        arr.extend(entries)


    matrix=np.array(arr).reshape(n,m)

    visited=np.array([False]*(n*m)).reshape(n,m)


    Floodfill(matrix,0,0," ",visited)


