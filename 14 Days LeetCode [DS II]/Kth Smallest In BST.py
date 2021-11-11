from BST.BuildBstFromArray import *





def kthSmallest(root, k):
        if root == None:
            return None

        que = []
        Inorder(root, que)

        return que[k - 1]


def Inorder(root, que):
    if root == None:
        return

    Inorder(root.left, que)

    que.append(root.data)

    Inorder(root.right, que)




if __name__ == '__main__':
    arr=[3,4,5,1,9,16]
    root = insertBST(None,arr[0])

    for i in range(1,len(arr)):
        insertBST(root,arr[i])

    print( kthSmallest(root,3))





