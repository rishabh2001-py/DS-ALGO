class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data


def search(inorder,start,end,curr):

    for i in range(start,end):

        if(inorder[i]==curr):
            return i

    return -1


def buildTree(pre,inorder,start,end,idx):

    if(start>end):
        return None
    curr=pre[idx]
    idx=idx+1
    node=Node()

    if(start==end):

        return node

    pos=search(inorder,start,end,curr)
    node.left=buildTree(pre,inorder,start,pos-1,idx)
    node.right=buildTree(pre,inorder,pos+1,end,idx)

    return node


def Inorder(root):
    if (root == None):
        return
    Inorder(root.left)
    print(root.data,end="--")
    Inorder(root.right)







pre=[1,2,4,5,3,6,7]
inorder=[4,5,2,1,6,7,3]
idx=0
root=Node()
root = buildTree(pre,inorder,0,len(inorder),idx)

Inorder(root)



