class LinkedList:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    curr = head
    slow = fast = LinkedList(None)
    fast.next = curr

    while (curr and curr.next):

        if curr.next.val == curr.val:

            while (curr and curr.next and (curr.next.val == curr.val)):
                curr = curr.next

            curr = curr.next
            slow.next = curr

        else:
            slow = slow.next
            curr = curr.next

    return fast.next


def LinkedListFromArray(arr):
    head = LinkedList(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = LinkedList(arr[i])
        temp = temp.next

    return head


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 4, 5, 5, 5,6,7,9,9,9,12]

    head = LinkedListFromArray(arr)
    deleteDuplicates(head)

    while head:
        print(head.val, end="-->")
        head = head.next
    print("None")
