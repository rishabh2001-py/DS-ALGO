class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data


def Count(root):
    if root == None:
        return 0

    return Count(root.left)+Count(root.right)+1

def Sum(root):

    if root ==None:
        return 0

    return Sum(root.left)+Sum(root.right)+root.data




if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(Count(root))

    print(Sum(root))
