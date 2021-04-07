
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLL:
    def __init__(self):
        self.head = None


    def insertion_at_head(self,data):
        new=Node(data)
        if(self.head==None):
            self.head=new
            return
        new.next=self.head
        self.head.prev=new

        self.head=new

    def insertion_at_tail(self,data):
        if self.head==None:
            self.insertion_at_head(data)
            return
        new=Node(data)
        temp=self.head
        while (temp.next):
            temp = temp.next
        new.prev=temp
        temp.next=new
    def insertion_at_specific(self,pos,data):
        if(pos==0):
            return
        if(pos==1):
            self.insertion_at_head(data)
            return
        new=Node(data)
        count=1
        temp=self.head
        while(count!=pos-1):
            temp=temp.next
            count+=1
        new.next=temp.next
        temp.next=new
        new.prev=temp
    def deletion(self,pos):
        temp=self.head
        if(self.head==None):
            print("List is empty")
            return
        if (pos == 1):
            self.head = self.head.next
            self.head.next.prev = None
            return
        count=1
        while(temp.next):
            if(count==pos):
                break
            count+=1
            temp=temp.next
        if(temp.next==None):
            temp.prev.next=None
            return
        temp.prev.next=temp.next
        temp.next.prev=temp.prev



    def display(self,head):
        if(self.head==None):
            print("DD IS EMPTY")
            return


        temp=self.head
        print(end="Null<-->")
        while(temp):
            print(temp.data,end="<-->")
            temp=temp.next
        print("Null")

    def reverse(self,head):

        if(self.head==None):
            return self.head
        if(self.head.next==None):
            return self.head

        current=self.head
        temp=None

        while(current):
            temp=current.prev
            current.prev=current.next
            current.next=temp

            current=current.prev

        if(temp):
            temp=temp.prev
        self.head=temp

        return self.head





if __name__ == '__main__':
    ob1=DoublyLL()
    ob1.display(ob1.head)
    ob1.insertion_at_tail(6)
    ob1.insertion_at_tail(2)
    ob1.insertion_at_tail(3)
    ob1.insertion_at_head(1)
    ob1.insertion_at_head(9)
    ob1.display(ob1.head)
    ob1.reverse(ob1.head)
    ob1.display(ob1.head)
















