#                            4
#                           /  \
#                          2    5
#                         / \   / \
#                        7   1  2  3
#                           /
#                          6

currsum=0
maxheight = 0

from RightViewOfBinaryTree import Node
def SumofNodesFromRootToLeaf(root,h,sum,arr):
    global currsum ,maxheight
    if root is None:
        return
    maxheight = max(maxheight, h)
    if root.left == None and root.right == None and maxheight==h:
        if h == maxheight:
            arr.append([sum+root.data,h])
    SumofNodesFromRootToLeaf(root.left,h+1,sum+root.data,arr)

    SumofNodesFromRootToLeaf(root.right,h+1,sum+root.data,arr)




    



if __name__ == '__main__':

    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(1)
    root.right.left = Node(2)
    root.right.right = Node(3)
    root.left.right.left = Node(6)
    root.left.right.right = Node(9)
    root.right.left.right = Node(1)
    res = []
    # ls = -10000
    # maxls = -100000
    arr=[]
    (SumofNodesFromRootToLeaf(root,0,0,arr))
    print(max(arr))



