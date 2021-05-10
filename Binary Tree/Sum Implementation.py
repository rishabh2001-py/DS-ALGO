class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def SumImplementation(root):
    if root == None:
        return

    SumImplementation(root.left)
    SumImplementation(root.right)
    if (root.left):
        root.data += root.left.data
    if (root.right):
        root.data += root.right.data


def Preorder(root):
    if (root == None):
        return
    print(root.data, end=" ")
    Preorder(root.left)
    Preorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    (Preorder(root))
    print()
    (SumImplementation(root))

    Preorder(root)
