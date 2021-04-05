class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None

    def insertATfront(self,head,data):
        new = Node(data)

        temp = self.head
        if (self.head == None):
            new.next = new
            self.head = new
            return
        while (temp.next != self.head):
            temp = temp.next
        temp.next = new
        new.next = self.head
        self.head = new


    def addINLAST(self,data):
        new = Node(data)
        temp = self.head
        if (self.head == None):
            self.insertATfront(self.head,data)
            return

        while (temp.next != self.head ):
            temp = temp.next
        temp.next = new
        new.next = self.head

    def display(self,head):
        temp=self.head
        if(self.head==None):
            print("List is EMPTY INSERT SOMETHING!!!")
        count=0
        while(temp!=self.head or count==0 ):
            count+=1
            print(temp.data,end="-->")
            temp=temp.next
        print(temp.data)
        print("Length is ",count)
    def removeElementByPosition(self,pos):
        temp=self.head
        count=1
        if(self.head==None):
            print("NO ELEMENT CANT DELETE")
            return
        if pos==1:
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=self.head.next
            self.head=self.head.next
            return
        while(count!=pos-1):
            temp=temp.next
            count+=1
        temp.next=temp.next.next
        return self.head









if __name__ == '__main__':
    ob1=circularLinkedList()
    ob1.addINLAST(4)
    ob1.addINLAST(1)
    ob1.insertATfront(ob1.head, 7)
    ob1.insertATfront(ob1.head, 3)
    ob1.insertATfront(ob1.head, 2)
    ob1.insertATfront(ob1.head,7)
    ob1.insertATfront(ob1.head, 3)
    ob1.insertATfront(ob1.head, 2)
    ob1.display(ob1.head)
    ob1.removeElementByPosition(1)
    ob1.display(ob1.head)


