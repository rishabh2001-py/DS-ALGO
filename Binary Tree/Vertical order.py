class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def VerticalOrder(root):
    m=dict()
    hd=0

    vertical(root,m,hd)
    for i in m:
        print(i,'::',m[i])

def vertical(root,m,hd):
    if root is None:
        return

    try:
        m[hd].append(root.data)
    except:
        m[hd]=[root.data]

    vertical(root.left,m,hd-1)
    vertical(root.right,m,hd+1)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    VerticalOrder(root)
