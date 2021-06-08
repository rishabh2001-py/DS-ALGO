#                            20
#                           /  \
#                          8    22
#                         / \   / \
#                        4  12 -5   25
#
#        o/p should be :       66
# #                           /  \
# #                          16    20
# #                         / \   / \
# #                        0  0  0   0
#
class Node:

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def toSumTree(root) :

    if(root is None):
        return 0

    ls =toSumTree(root.left)
    rs =toSumTree(root.right)
    temp =root.data
    root.data= ls +rs

    return ls +rs +temp


def Inorder(root):
    if (root == None):
        return
    Inorder(root.left)
    print(root.data,end="--")
    Inorder(root.right)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.left = Node(-5)
    root.right.right = Node(25)
    (toSumTree(root))
    Inorder(root)







