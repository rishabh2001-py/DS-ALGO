class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data


def fillmap(root,l,d,m):
    if root is None:
        return

    if d not in m:
        m[d]=[root.data,l]
    elif(m[d][1]>l):
        m[d]=[root.data,l]
    fillmap(root.left,l+1,d-1,m)
    fillmap(root.right, l + 1, d + 1, m)








def TopView(root):


    if root is None:
        return
    m={}
    fillmap(root,0,0,m)

    for i in sorted(m.keys()):
        print(m[i][0],end=" ")









if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(TopView(root))