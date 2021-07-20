class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def KDistance(root, k):
    if root is None:
        return

    res = []

    que = []
    que.append(root)
    que.append(None)
    h = 1

    while (len(que) != 0):

        Node = que.pop(0)

        if (Node != None):
            if (h == k and Node != None):
                res.append(Node.data)

            if Node.left:
                que.append(Node.left)

            if Node.right:
                que.append(Node.right)

        elif (len(que) != 0):

            que.append(None)

            h += 1

            if (h == k and Node!=None):
                res.append(Node.data)



    return res


if __name__ =='__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(KDistance(root,3))







