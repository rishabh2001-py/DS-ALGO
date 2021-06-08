from PRE_POST_IN_ORDER_TRAVERSAL import Inorder


class Node:

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


f = 0


def isSumTree(root):
    f = 1
    if root is None:
        return
    solve(root)
    return f


def solve(root):
    global f
    if root == None:
        return 0
    if f == 0:
        return 0
    if root.left == None and root.right == None:
        return root.data

    a = solve(root.left)
    b = solve(root.right)

    check = a + b

    if (check != root.data):
        f = 0

    return a + b + root.data


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.left = Node(-5)
    root.right.right = Node(25)

    Inorder(root)
    print()
    print("Tree is %2d " % (isSumTree(root)))
