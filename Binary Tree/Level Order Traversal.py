
def levelOrder(root):
        ls = []
        que = []
        que.append(root)
        que.append(None)

        while (len(que) != 0):

            node = que[0]
            que.pop(0)

            if (node != None):

                ls.append(node.data)

                if (node.left):
                    que.append(node.left)

                if (node.right):
                    que.append(node.right)

            elif (len(que) != 0):

                que.append(None)

        return ls


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None


if __name__ =='__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(levelOrder(root))
