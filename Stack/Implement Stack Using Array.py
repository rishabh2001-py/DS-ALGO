class Stack:

    def __init__(self):
        arr = []
        self.arr = arr

    def push(self, data):
        self.arr.append(data)
        return self.arr

    def isEmpty(self):
        if (len(self.arr) != 0):
            return "Not Empty"
        return "Stack is Empty"

    def pop(self):
        if (len(self.arr) == 0):
            return(self.isEmpty())
        else:
            ele = self.arr.pop()
            return ele

    def peek(self):
        if (len(self.arr) == 0):
            self.isEmpty()
        return self.arr[len(self.arr) - 1]
    def display(self):
        if(len(self.arr)==0):
            return(self.isEmpty())
        else:
            return self.arr

if __name__ == '__main__':
    ob = Stack()
    ob.push(4)
    ob.push(2)
    ob.push(3)
    ob.push(1)
    ob.push(9)
    ob.push(8)
    ob.push(4)
    ob.push(2)
    ob.push(3)
    ob.push(1)
    ob.push(9)
    ob.push(8)
    print(ob.display())
    print(ob.pop())
    print(ob.pop())
    print(ob.pop())
    print(ob.display())
