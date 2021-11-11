#Adjancy Matrix
#List
#Maps

#AdjancyMatrix

def BuildAdjMat(adj,u,v):


    adj[u][v] = 1
    adj[v][u] = 1

def BuildUsingMaps(Map,u,v):


    try:
        Map[u].add(v)
        Map[v].add(u)

    except :
        if u not in  Map.keys():
            Map[u] = set()

        if v not in Map.keys():
            Map[v] = set()

        Map[u].add(v)
        Map[v].add(u)





if __name__ == "__main__":

    vertices,edges = map(int,input().strip().split())
    # adj = [[0]*(edges+1)]*(edges+1)
    # # print(adj)
    # for i in range(edges):
    #
    #     u,v =  map(int,input().strip().split())
    #
    #     BuildAdjMat(adj,u,v)
    #
    # for i in range(edges):
    #     print(adj[i])

    m = {}

    for  i in range(edges):
        u,v =  map(int,input().strip().split())

        BuildUsingMaps(m,u,v)

    print(m)










