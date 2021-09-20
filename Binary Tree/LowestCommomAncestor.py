


from CountNodesGreaterThanX import  Node


def lca(root, n1, n2):
    if root is None:
        return None

    path1 = []
    path2 = []
    pNode = Node(-1)
    if getPath(root, n1, path1) and getPath(root, n2, path2):

        for i in range(min(len(path1), len(path2))):

            if path1[i].data != path2[i].data:
                return pNode

            pNode = path1[i]

    return pNode


def getPath(root, key, path):
    if root == None:
        return False

    if root.data == key:
        path.append(root)
        return True

    path.append(root)

    if getPath(root.right, key, path):
        return True

    if getPath(root.left, key, path):
        return True

    path.pop()

    return False




if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    res = (lca(root,6,7))
    print(res.data)
