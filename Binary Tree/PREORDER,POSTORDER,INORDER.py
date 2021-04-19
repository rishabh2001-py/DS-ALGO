class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data

def Preorder(root):
    if root==None:
        return

    print(root.data,end= "--")
    Preorder(root.left)
    Preorder(root.right)

def PostOrder(root):

    if(root==None):
        return
    PostOrder(root.left)
    PostOrder(root.right)

    print(root.data,end="--")
def Inorder(Root):
    if (root == None):
        return
    PostOrder(root.left)
    print(root.data,end="--")
    PostOrder(root.right)






if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    Preorder(root)
    print()

    PostOrder(root)
    print()

    Inorder(root)
    print()








