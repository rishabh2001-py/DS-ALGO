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
    ls=[]
    if(root==None):
        return ls

    PostOrder(root.left)
    PostOrder(root.right)
    ls.append(root.data)

def Inorder(root):
    if (root == None):
        return
    if root.left == None:
        print("NL",end ="--")
    if root.right == None:
        print("NR",end ="--")
    Inorder(root.left)
    print(root.data,end="--")
    Inorder(root.right)






if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    # root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)


    Inorder(root)
    print()










