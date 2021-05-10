class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if (root == None):
        return 0

    lheight = height(root.left)
    rheight = height(root.left)

    return max(lheight+1, rheight+1)


root = Node(1)

root.left = Node(2)
root.right = Node(3)

print("Height is:", height(root))
