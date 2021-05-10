

class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data


def reverseLevelOrder(root):
    if root == None:
        return

    qu = []
    ls = []
    qu.append(root)
    qu.append(None)

    while (len(qu) != 0):
        node = qu[0]
        qu.pop(0)

        if (node != None):
            ls.append(node.data)
            if node.right:
                qu.append(node.right)
            if node.left:
                qu.append(node.left)
        elif (len(qu) != 0):

            qu.append(None)

    ls.reverse()

    return ls












if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(reverseLevelOrder(root))


