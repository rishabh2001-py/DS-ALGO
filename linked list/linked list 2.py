'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''

#Given a singly linked list, remove all the nodes which have a greater value on its following nodes.
class Solution:
    def compute(self, head):
        current = head
        nextptr = None
        prev = None
        while (current):
            nextptr = current.next
            current.next = prev

            prev = current
            current = nextptr
        n1 = prev
        leader = prev.data
        while (n1.next and n1):
            if (n1.data >= leader):
                leader = n1.data
                n1 = n1.next
            else:
                n1.data = n1.next.data
                n1.next = n1.next.next
        current = prev
        nextptr = None
        prev = None
        while (current):
            nextptr = current.next
            current.next = prev

            prev = current
            current = nextptr
        if (prev == None or prev.next == None):
            return prev
        if ((prev.next.data > prev.data)):
            prev = prev.next
        return prev

    # {


#  Driver Code Starts
# Initial Template for Python 3


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def getNode(self, value):  # return node with given value, if not present return None
        curr_node = self.head
        while (curr_node.next and curr_node.data != value):
            curr_node = curr_node.next
        if (curr_node.data == value):
            return curr_node
        else:
            return None

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


if __name__ == "__main__":
    t = int(input(" test case"))
    while (t > 0):
        n = int(input("length"))
        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)

        result = Solution().compute(a.head)
        a.head = result
        a.printList()
        t -= 1

# } Driver Code Ends