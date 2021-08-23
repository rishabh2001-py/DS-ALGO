from BfsUsingMaps import graphMap as Gm


def DfsUtil(source, destination, visited):
    if source == destination:
        return True

    for neighbour in graph.map[source]:
        if visited[neighbour] == False:
            visited[neighbour] = True
            IsTrue = DfsUtil(neighbour, destination, visited)
            if IsTrue:
                return True

    return False

def dfsPath(source,visited):
    
    visited.add(source)
    print(source,end="-->")
    
    for i in graph.map[source]:
        
        if i not in visited:
            dfsPath(i,visited)

            

def dfs(source, destination):
    visited = graph.vertex * [False]

    IsConnected = DfsUtil(source, destination, visited)

    return IsConnected


if __name__ == '__main__':
    graph = Gm(5)
    graph.addEdges(0, 1)
    graph.addEdges(1, 2)
    graph.addEdges(2, 3)
    graph.addEdges(3, 4)
    graph.addEdges(4, 2)
    graph.addEdges(4, 0)
    print(graph.map)
    print(dfs(0, 2))
    
    dfsPath(0,set())
