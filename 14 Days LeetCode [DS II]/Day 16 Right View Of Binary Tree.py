class Tree:

    def __init__(self,val=0):

        self.val = val
        self.left  = None
        self.right = None


def rightSideView(root):
    if root == None:
        return []

    que = []

    que.append(root)

    res = []

    while (len(que) != 0):

        n = len(que)

        for i in range(n):

            if i == n - 1:
                res.append(que[0].val)

            node = que.pop(0)
            if node.left:
                que.append(node.left)

            if node.right:
                que.append(node.right)

    return res


if __name__ == "__main__":

    node = Tree(1)
    node.left = Tree(2)
    node.right = Tree(3)

    print(rightSideView(node))







