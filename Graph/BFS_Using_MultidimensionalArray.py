class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        res = []
        que = []
        que.append(0)
        visited = len(adj) * [False]

        while (que):
            cur = que.pop(0)
            res.append(cur)
            for i in adj[cur]:

                if visited[i] == False:
                    que.append(i)
                    visited[i] = True
        return res


if __name__ == '__main__':

        V, E = map(int, input("Enter Vertices and Edges :: ").split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input("Enter source and Destination :").split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
