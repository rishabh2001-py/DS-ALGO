from RightViewOfBinaryTree import Node

def TreeAtSameLevelOrNot(root, res, h):
    if (root == None):
        return

    TreeAtSameLevelOrNot(root.left, res, h + 1)

    if root.left == None and root.right == None:
        res.append(h)

    TreeAtSameLevelOrNot(root.right, res, h + 1)


if __name__ == '__main__':

    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    # root.right.left = Node(-5)
    # root.right.right = Node(25)
    res = []
    TreeAtSameLevelOrNot(root, res, 1)
    print(res)

    if len(set(res)) == 1:
        print("Same Level")
    else:
        print("Not at Same Level")
