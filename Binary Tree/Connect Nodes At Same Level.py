from RightViewOfBinaryTree import levelOrder
class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.nextRight = None
        self.data = data
def connect(root):
    que = []

    que.append(root)

    while (que):

        n = len(que)
        # print(n)
        for i in range(n):

            node = que.pop(0)

            if node.left:
                que.append(node.left)

            if node.right:
                que.append(node.right)

            if i == n - 1:
                node.nextRight = None
            else:
                # print(node.data)
                node.nextRight = que[0]




if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    connect(root)
    print(levelOrder(root))

