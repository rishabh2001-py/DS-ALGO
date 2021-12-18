from RightViewOfBinaryTree import Node


def hasPathSum(root, S):
    def Ispath(root, S, curSum,res,tempArr):

        if root == None:
            return

        curSum += root.data


        Ispath(root.left, S, curSum,res,tempArr+[root.data])
        Ispath(root.right, S, curSum,res,tempArr+[root.data])

        if root.left == None and root.right == None:
            # print(s[0==curSum],curSum)
            tempArr =  tempArr+[root.data]
            if(S[0] == curSum):
                res.append(tempArr)

        curSum -= root.data
        # tempArr.pop()


        return False

    Sar = [S]
    res = []
    ans = Ispath(root, Sar, 0,res,[])
    print(res)


    return ans


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(4)
    root.right.left = Node(1)
    root.right.right = Node(7)

    print(hasPathSum(root,7))



