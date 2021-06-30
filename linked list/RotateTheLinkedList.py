class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):

        temp = head
        count = 0
        while (temp.next):
            count += 1
            temp = temp.next
        leng = count + 1
        if leng == k:
            return head
        lastnode = temp
        count = 0
        bnode = head
        k = k % leng

        while (count < k - 1):
            count += 1
            bnode = bnode.next

        # print(bnode.data)

        lastnode.next = head
        temphead = bnode.next
        bnode.next = None

        head = temphead

        return head




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == "__main__":
        n = int(input("Enter Length:"))
        arr = [int(x) for x in input().split()]
        k = int(input("Enter Rotation value :"))

        lis = LinkedList()
        for i in arr:
            lis.insert(i)

        head = Solution().rotate(lis.head, k)
        printList(head)
