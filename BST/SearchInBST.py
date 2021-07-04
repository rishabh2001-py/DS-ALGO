from BuildBstFromArray import Node , Inorder 


def Search(root,val):
    
    if root == None:
        return False
    
    if root.data == val:
        return True
    
    if val < root.data:
        answer = Search(root.left,val)
        return answer
    
    answer = Search(root.right,val)
    
    return answer
        
    




if __name__ == '__main__':
    root = Node(7)
    root.left = Node(4)
    root.right = Node(11)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(9)
    root.right.right = Node(12)
    arr = [7,4,11,2,4,7,8,9,12]
    for i in range(len(arr)):
        answer = Search(root,arr[i])
        if(answer == True):
            print(arr[i]," ELEMENT FOUND")
        else:
            print(arr[i], " NOT FOUND")



    
    
    