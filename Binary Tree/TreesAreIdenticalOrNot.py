class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def isIdentical(root1, root2):
    l1 = []
    l2 = []
    Inorder(root1, l1)
    Inorder(root2, l2)
    return (l1 == l2)


def Inorder(root, l):
    if root == None:
        return

    if root.left == None:
        l.append("L")
    if root.right == None:
        l.append("R")
    Inorder(root.left, l)
    l.append(root.data)
    Inorder(root.right, l)


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    print(isIdentical(root, root1))

