#                            1
#                           /  \
#                          2    5
#                         / \    \
#                        4   5     2
#                                 / \
#                                4   5
#
from RightViewOfBinaryTree import Node

def Check(root):
    if root == None:
        return
    m={}
    helper(root,m)
    print(m)
    f=False
    for i in m.values() :
        if i >= 2:
            print('Subtree Present')
            f = True
            break;
    if f == False:
        print("Subtree not found")






def helper(root,m):

    if root is None :
        return "_"
    s=""

    if root.left  == None and root.right == None:
        s=str(root.data)
        return s
    s= s + str(root.data)
    s= s+ helper(root.left,m)
    s = s + helper(root.right,m)
    try:
        m[s]+=1
    except:
        m[s]=1
    return s







if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.right.left = Node(2)
    root.right.right = Node(2)
    root.right.right.left= Node(4)
    root.right.right.right = Node(5)
    # root.right.left.right = Node(1)
    Check(root)