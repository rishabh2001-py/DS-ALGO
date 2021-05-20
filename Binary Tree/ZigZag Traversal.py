class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ZigZag(root):
    a=[]

    if root is None:
        return a

    que=[]
    que.append(root)
    v=[]
    flag=1

    while(len(que)!=0):

        n=len(que)

        for i in range(n):
            node=que[0]
            v.append(node.data)
            que.pop(0)

            if(node.left):
                que.append(node.left)
            if (node.right):
                que.append(node.right)

        if(flag==1):
            a.extend(v)
            v=[]
            flag=0
        else:
            v.reverse()
            a.extend(v)
            flag=1
            v=[]
    print(a)












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
    ZigZag(root)