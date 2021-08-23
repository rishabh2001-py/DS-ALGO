def detectCycle(adj, v):
    visited = [0] * v

    for i in range(v):
        if (visited[i] == 0 and isCycle(adj, i, visited, -1)):
            return True
    print(visited)
    return False



def isCycle(adj, source, visited, parent):

    visited[source] = 1

    for i in adj[source]:
        if i != parent:
            if (visited[i] == 1):
                return True

            if (visited[i] == 1 and isCycle(adj, i, visited, source)):
                return True

    return False



if __name__ == '__main__':
    v, edges = map(int, input("Enter Vertices: ").split())
    adj =[[] for i in range(v)]

    for i in range(edges):
            source, destination = map(int, input('Enter Edges ').split())
            adj[destination].append(source)
            adj[source].append(destination)

    print(adj)
    m = {}
            # for i in range(len(adj)):
            #      m[i] = adj[i]
            # print(m)

    print(detectCycle(adj, v))
