class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = [None]*V

    def add_edge(self,source,destination):

        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source]=node

        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def printGraph(self):

        for i in range(self.V):
            temp = self.graph[i]
            print(i,end="-->")
            while temp:
                print("  ",temp.vertex,end="")
                temp = temp.next
            print()

if __name__ == '__main__':
    V=5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.printGraph()





































