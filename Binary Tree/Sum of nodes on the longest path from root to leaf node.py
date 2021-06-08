from RightViewOfBinaryTree import Node

def SumofNodesFromRootToLeaf(root,Ls,maxls):
    if root is None:
        return
    SumofNodesFromRootToLeaf(root.left,Ls + root.data,maxls)
    if root.left ==  None and root.right == None:
        maxls=max(Ls,maxls)
    SumofNodesFromRootToLeaf(root.left,Ls+root.data,maxls)


if __name__ == '__main__':

    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    # root.right.left = Node(-5)
    # root.right.right = Node(25)
    res = []
    ls = -10000
    maxls = -100000
    SumofNodesFromRootToLeaf(root,ls,maxls)


