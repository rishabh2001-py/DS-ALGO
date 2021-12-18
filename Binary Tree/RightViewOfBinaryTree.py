class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data


def levelOrder(root):
        ls = []
        que = []
        que.append(root)
        que.append(None)

        while (len(que) != 0):

            node = que[0]
            que.pop(0)

            if (node != None):

                ls.append(node.data)

                if (node.left):
                    que.append(node.left)

                if (node.right):
                    que.append(node.right)

            elif (len(que) != 0):

                que.append(None)

        return ls

def rightView(root):
    if root == None:
        return -1
    que = []

    que.append(root)

    while (len(que) != 0):

        n = len(que)

        for i in range(0,n):
            node = que[0]
            que.pop(0)

            if (i == (n - 1)):
                print(node.data,end=' ')

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)


if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    #root.left.left = Node(4)
    #root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(rightView(root))