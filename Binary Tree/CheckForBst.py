# A Tree is a Binary Search Tree only if its Inorder traversal is in sorted Ascending order



class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

def isBST(root):
        arr = []
        Inorder(root, arr)
        print(arr)
        for i in range(len(arr) - 1):
            if (arr[i] >= arr[i + 1]):
                return False
        return True


def Inorder(root, arr):
    if root == None:
        return
    Inorder(root.left,arr)
    arr.append(root.data)
    Inorder(root.right,arr)



if __name__ == '__main__':

    root = Node(7)
    root.left = Node(4)
    root.right = Node(11)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(9)
    root.right.right = Node(12)
    print(isBST(root))

