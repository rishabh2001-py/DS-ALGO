class StackNodes:
    def __init__(self, head=None, next=None):
        self.data = head
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, data):
        new = StackNodes(data)
        if (self.bottom == None):
            self.bottom = new
            self.top = self.bottom
        else:
            self.top.next = new
            self.top = new

    def isEmpty(self):
        if (self.top == None):
            return -1
        return

    def pop(self):

        if (self.isEmpty() == -1):
            return "-1,cant POP, Underflow"
        else:
            temp = self.bottom
            while (temp.next != self.top):
                temp = temp.next
            popped = temp.next.data
            temp.next = None
            self.top = temp

            return popped

    def display(self):
        if (self.bottom == None):
            print("Empty")
            return
        else:
            temp = self.bottom
            while (temp):
                print(temp.data, end="---")
                temp = temp.next
            print("Null")

    def peek(self):
        if (self.isEmpty() == -1):
            return "-1 UnderFlOW"
        else:
            return self.top.data


if __name__ == '__main__':
    ob = Stack()
    ob.display()
    ob.push(4)
    ob.push(3)
    ob.push(5)
    ob.push(6)
    ob.push(11)
    ob.push(12)
    ob.push(13)
    ob.display()
    print(ob.pop())
    ob.display()
    print(ob.pop())
    ob.display()
    print(ob.pop())
    print(ob.pop())
    print(ob.peek())
    ob.display()
