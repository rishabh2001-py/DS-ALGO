class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data



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

            if (i == 0 ):
                print(node.data,end=' ')
            

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)


if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(rightView(root))