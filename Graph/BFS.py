from GraphImplementation import AdjNode,Graph


class Bfs(Graph):

    def search(self,source,destination):
        que = []
        visited = self.V*[False]
        visited[source] = True
        parent = self.V*[-1]
        que.append(source)

        while(len(que)!=0):
            cur = que.pop(0)
            if cur == destination:
                break;

            for i in range(self.graph[cur]):
                if not visited[i]:
                    que.append(i)
                    visited[i]=True
                    parent[i]=cur

        cur = destination
        dist = 0

        while(parent[cur]!=-1):
            print(cur,"-->",)
            cur = parent[cur]
            dist+=1
        
        
        


if __name__ == '__main__':

    
    V = int(input("Enter Number of Vertex:: "))
    graph = Bfs(V)
    E = int(input("Enter Edges:: "))
    for i in range(E):
        src,dest = map(int,input('Enter src and Destination ').strip().split())
        graph.add_edge(src,dest)
    
    src,dest = map(int,input('Enter bfs src snd destination : ').strip().split())
    graph.search(src,dest)    

    


        
        
        




