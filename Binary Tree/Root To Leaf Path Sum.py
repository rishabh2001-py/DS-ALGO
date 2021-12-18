from RightViewOfBinaryTree import Node


def hasPathSum(root, S):
    def Ispath(root, S, curSum):

        if root == None:
            return False

        curSum += root.data

        if (Ispath(root.left, S, curSum)):
            return True
        if (Ispath(root.right, S, curSum)):
            return True
        if root.left == None and root.right == None:
            # print(s[0==curSum],curSum)

            return (S[0] == curSum)

        curSum -= root.data

        return False

    Sar = [S]

    ans = Ispath(root, Sar, 0)

    return ans


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(hasPathSum(root,10))
    print(hasPathSum(root,11))
    print(hasPathSum(root,5))


