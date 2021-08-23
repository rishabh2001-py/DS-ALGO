count = 0

class Node:

    def __init__(self,data=None):

        self.left=None
        self.right=None
        self.data=data



def CountNodesGreaterThanX(root,x):
    global count
    if root is None:
        return 0

    CountNodesGreaterThanX(root.left,x)

    if root.data > x:
        count+=1

    CountNodesGreaterThanX(root.right,x)

    return count











if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(CountNodesGreaterThanX(root,2))
    # print(count)
