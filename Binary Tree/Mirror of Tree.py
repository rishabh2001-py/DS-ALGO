class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def Mirror(root,mirrorRoot):
     if (root==None):
         mirrorRoot=None
         return mirrorRoot
     mirrorRoot=Node(root.data)

     if(root.left):
         mirrorRoot.right=Mirror(root.left,mirrorRoot.right)

     if (root.right):
         mirrorRoot.left = Mirror(root.right, mirrorRoot.left)
     return mirrorRoot








def Preorder(root):
    if (root == None):
        return
    print(root.data, end=" ")
    Preorder(root.left)
    Preorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print('Original Tree:',end=" ")
    (Preorder(root))
    print()
    mirrorRoot=None
    mirrorRoot=Mirror(root,mirrorRoot)
    print('Mirror Tree:',end=" ")
    Preorder(mirrorRoot)



