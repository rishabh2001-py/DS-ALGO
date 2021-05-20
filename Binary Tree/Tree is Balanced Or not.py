class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data


def isBalanced(root):
    if root == None:
        return True

    lheight = ch(root.left)
    rheight = ch(root.right)

    dif = abs(lheight - rheight)

    if (dif > 1):
        return False
    else:
        return (isBalanced(root.left) and isBalanced(root.right))


def ch(root):
    if root == None:
        return 0

    lheight = ch(root.left)
    rheight = ch(root.right)

    return (max(lheight + 1, rheight + 1))










if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    #root.left.right = Node(5)
    root.right.left = Node(6)
    #root.right.right = Node(7)
    #root.right.left.right = Node(8)
    #root.right.right.right = Node(9)
    print(isBalanced(root))