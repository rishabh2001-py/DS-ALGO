class LinkedList :

    def __init__(self,val = None,next = None):

        self.val = val
        self.next = next





def deleteDuplicates(head):
    while head.next:

        if head.val == head.next.val:
            head = head.next
        else:
            break

    fast = head
    slow = head

    while (fast.next):

        if fast.next.val == slow.val:
            fast = fast.next
            slow.next = fast.next
        else:
            # slow.next = fast.next
            fast = fast.next
            slow = slow.next

    return head


def LinkedListFromArray(arr):

    head = LinkedList(arr[0])
    temp =head
    for i in range(1,len(arr)):
        temp.next = LinkedList(arr[i])
        temp = temp.next

    return head






if __name__ == '__main__':

   # Node = LinkedList(1)
   # Node.next = LinkedList(2)
   # Node.next.next = LinkedList(3)
   # Node.next.next.next = LinkedList(3)
   # Node.next.next.next.next = LinkedList(5)
   # Node.next.next.next.next.next = LinkedList(5)

   arr = [1,2,3,4,4,5,5,5]

   head = LinkedListFromArray(arr)

   deleteDuplicates(head)
   while head:
       print(head.val,end = "-->")
       head = head.next
   print("None")