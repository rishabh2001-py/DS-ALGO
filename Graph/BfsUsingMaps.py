
class graphMap:

    def __init__(self,vertex):
        self.map = {}
        self.vertex = vertex
        for i in range(self.vertex):
            self.map[i] = []

    def addEdges(self,source,destination):

        self.map[source].append(destination)
        self.map[destination].append(source)

    def display(self):
        print(self.map)


def BFS(graph,source,destination):

    que = []
    que.append(source)
    visited = graph.vertex * [False]
    visited[source]= True
    parent = graph.vertex * [-1]

    while(len(que)!=0):

        cur = que.pop(0)
        if cur == destination:
            break;
        # print(cur)

        for neighbour in graph.map[cur] :
            if visited[neighbour] == False:
                que.append(neighbour)
                visited[neighbour] = True
                parent[neighbour] = cur

    cur = destination
    dist = 0
    # print(parent)
    while (parent[cur] != -1):
        print(cur, "-->",end =" " )
        cur = parent[cur]
        dist += 1
    print(source)

    print("Shortest distance is ",dist)







if __name__ == '__main__':
    graph = graphMap(5)
    graph.addEdges(0, 1)
    graph.addEdges(1, 2)
    graph.addEdges(2, 3)
    graph.addEdges(3, 4)
    graph.addEdges(4, 2)
    graph.addEdges(4, 0)
    # graph.display()
    BFS(graph,1,3)






