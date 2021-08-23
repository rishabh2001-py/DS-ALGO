from CountNodesGreaterThanX import  Node

path = []
def Search(root,x):

    if root is None :
        return False

    if root.data ==x:
        return True

    IsFound=Search(root.left,x)
    if IsFound:
        return True

    IsFound=Search(root.right,x)
    if IsFound:
        return True

    return False

def printPath(root,x):
    global path
    if root is None :
        return False

    if root.data == x:
        print(root.data)
        path.append(root.data)
        return True

    IsFound=Search(root.left,x)

    if IsFound:
        print(root.data)
        path.append(root.data)
        return True

    IsFound=Search(root.right,x)

    if IsFound:
        print(root.data)
        path.append(root.data)
        return True

    return False










if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    Isfound=(Search(root,7))
    print(Isfound)

    if Isfound :
        printPath(root,1)

    print(path)

