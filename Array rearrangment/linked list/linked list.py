class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head = None

    def show(self):
        n = self.head
        while (n):
            print(n.data, end="-->")
            n = n.next
        print("NULL")

    def push(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def length(self):
        n = self.head
        count = 0
        if (self.head == None):
            return "Empty list"
        while (n):
            count = count + 1
            n = n.next
        return count

    def append(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode

        else:
            n=self.head
            while(n.next):
                n=n.next
            n.next=newnode
        return   self.head




        # def pop(self):
    # if(ob1.length()==0):
    # return "list is empty"
    # n=self.head

    def removeDuplicates(self, head):
        n = self.head
        l1 = []
        while (n.next):
            uniq = set()

            node = head

            while node.next is not None:
                uniq.add(node.data)
                if node.next.data in uniq:
                    node.next = node.next.next
                else:
                    node = node.next
            return head

    def last2First(self, head):
        # [1,2,3,4]
        # [4,1,2,3]
        n = self.head
        sec_last = None
        while n.next and n:
            sec_last = n
            n = n.next

        sec_last.next = None

        n.next = self.head
        self.head = n

        return head

    def reverse(self, head):
        prev = None
        nextptr = None
        current = self.head
        while (current):
            nextptr = current.next
            current.next = prev

            prev = current
            current = nextptr
        self.head = prev
        return head

    def reverseK(self, head, k):
        nextptr = None
        prev = None
        current = self.head
        count = 0
        while (current and count < k):
            nextptr = current.next
            current.next = prev

            prev = current
            current = nextptr

            count += 1
        if (nextptr!=None):
            head.next = self.reverseK(nextptr,k)
            print("jk")

        return prev


def multiplyTwoList(head1, head2):
    s = ""
    s2 = ""
    while (head1):
        s = s + str(head1.data)

        head1 = head1.next
    while (head2):
        s2 = s2 + str(head2.data)

        head2 = head2.next
    res = int(s) * int(s2)
    return res


def findIntersection(head1, head2):

    new=node(None)
    head=None
    n1=head1
    n2=head2

    while(n1 or n2):
        new=node(n1.data)
        if(n1.data>n2.data):
            n2=n2.next
        elif(n1.data<n2.data):
            n1=n1.next
        else:
             if(head==None):
                 head=new
                 n=head
             else:
                 n.next=new
             n1=n1.next
             n2=n2.next
    while(head):
        print(head.data,end="-->")
        head=head.next












ob1 = linklist()
ob2 = linklist()
ob1.push(1)
ob1.append(2)
ob1.push(3)
ob2.append(1)
ob2.append(1)
ob2.append(3)
ob1.show()
ob2.show()
findIntersection(ob1.head,ob2.head)


# ob2.show()
# print("")
# ob1.show()
# print("")

# res=multiplyTwoList(ob1.head,ob2.head)
# print("RESULTANT OF BOTH LL",res)
