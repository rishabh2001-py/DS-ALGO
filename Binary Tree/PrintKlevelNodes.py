from CountNodesGreaterThanX import Node


def KlevelNodes(root,x):
    
    if root == None:
        return
    
    
    if x == 1:
        print(root.data)
    
    KlevelNodes(root.left,x-1)
    KlevelNodes(root.right,x-1)
    

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.right = Node(25)
    root.left.right.left=Node(10)
    root.left.right.right=Node(14)
    
    KlevelNodes(root,3)
    
    