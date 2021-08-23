
def addEdges(adj,source,destination):

    adj[source].append(destination)
    adj[destination].append(source)


def  NumberOfConnectedEdges(adj):
    components = []
    visited = [False] * (len(adj))
    for i in range(len(adj)):
        if visited[i]==False:
            comp = []
            getConnectedTree(adj,i,visited,comp)
            components.append(comp)
    print(components)
    print("There are  componensts in this graph",len(components))


def getConnectedTree(adj,source,visited,comp):

    visited[source] = True
    comp.append(source)

    for neighbor in adj[source]:
        if visited[neighbor] == False :
            getConnectedTree(adj,neighbor,visited,comp)





if __name__ == '__main__':

    vert = int(input("Enter Number of Vertices "))
    adj = [[] for i in range(vert)]
    Edges = int(input("Enter the Edsges :"))

    for i in range(Edges):
        u,v = map(int,input('Enter source and destination :').split())
        addEdges(adj,u,v)


    NumberOfConnectedEdges(adj)


