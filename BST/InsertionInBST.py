from SearchInBST import Node ,Inorder


def insert(root,key):
    if root == None:
        root = Node(key)
        return root

    answer = search(root, key)
    print(answer)
    if answer == False:
        insertsol(root, key)

    return root


def search(root, key):
    if root == None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


def insertsol(root, key):
    if root == None:
        root = Node(key)

        return root

    if key < root.data:
        root.left = insertsol(root.left, key)

    if key > root.data:
        root.right = insertsol(root.right, key)

    return root




if __name__ == '__main__':
    root = Node(7)
    root.left = Node(4)
    root.right = Node(11)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(9)
    root.right.right = Node(12)
    Inorder(root)
    print()
    root=insert(root,6)
    Inorder(root)











