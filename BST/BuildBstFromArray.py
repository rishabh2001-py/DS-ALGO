
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insertBST(root,val):

    if root == None:
        root = Node(val)
        return root
    if val < root.data:
        root.left = insertBST(root.left,val)
    else:
        root.right = insertBST(root.right,val)

    return root


def Inorder(root):
    if root == None:
        return

    Inorder(root.left)
    print(root.data,end =" ")
    Inorder(root.right)


if __name__ == '__main__':
    arr=[3,4,5,1,9,16]
    root = insertBST(None,arr[0])

    for i in range(1,len(arr)):
        insertBST(root,arr[i])
    print('Inorder of BST:--',end=" ")
    Inorder(root)






