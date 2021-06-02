class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def LargestSumPath(root):

    util.maxsum = - 10**9
    util(root)
    return util.maxsum


def util(root):

    if root is None:
        return 0

    left = util(root.left)
    right = util(root.right)

    maxsingle= max(root.data + right,root.data+left,root.data)
    maxtop = max(maxsingle,root.data + left + right)

    util.maxsum = max(maxtop,util.maxsum)

    return maxsingle

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    print(LargestSumPath(root))