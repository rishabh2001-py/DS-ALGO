 # Given a Binary Tree, print the diagonal traversal of the binary tree.
# Consider lines of slope -1 passing between nodes.
# Given a Binary Tree, print all diagonal elements in a binary tree belonging to same line.
#                            20
#                           /  \
#                          8    22
#                         / \   / \
#                        4  12    25
#                           / \
#                          10  14
#output = 20 22 25 8 12 14 4 10


class Node:

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

def diagonal(root):
    que = []
    if root == None:
        return que

    que.append(root)
    res = []

    while (len(que) != 0):

        temp = que[0]
        que.pop(0)

        while (temp):

            if temp.left:
                que.append(temp.left)
            res.append(temp.data)
            temp = temp.right

    return res



if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.right = Node(25)
    root.left.right.left=Node(10)
    root.left.right.right=Node(14)
    print(diagonal(root))
