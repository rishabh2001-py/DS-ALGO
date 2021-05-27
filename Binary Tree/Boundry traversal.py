#                            20
#                           /  \
#                          8    22
#                         / \   / \
#                        4  12    25
#                           / \
#                          10  14
#    o/p should be : 20 8 4 10 14 25 22
#     it should print boundry of tree in anticlockwise left to right
#      we created 3 functions : left boundry ,right boundry and leaf nodes.

class Node:

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


# ----- MAIN FUNCTION---#

def printBoundaryView(root):
    res=[]
    res.append(root.data)
    left(root.left, res)
    leafnode(root, res)
    right(root.right, res)

    return res

# Left boundry function

def left( root, res):
    if root is None:
        return

    if root.left:
        res.append(root.data)
        left(root.left, res)
    elif root.right:
        res.append(root.data)
        left(root.right, res)

# Right boundry
def right(root, res):
    if root is None:
        return

    if root.right:
        right(root.right, res)
        res.append(root.data)
    elif root.left:
        right(root.left, res)
        res.append(root.data)

# LEAF nodes
def leafnode(root, res):
    if root is None:
        return
    leafnode(root.left, res)

    if root.left == None and root.right == None:
        res.append(root.data)

    leafnode(root.right, res)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.right = Node(25)
    root.left.right.left=Node(10)
    root.left.right.right=Node(14)
    print(printBoundaryView(root))
