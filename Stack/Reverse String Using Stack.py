
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

def reverse(s):
    ob=Stack()
    rev=""
    for i in range(len(s)):
        ob.push(s[i])
    for j in range(len(s)):
        rev=rev+ob.pop()
    return rev





if __name__ == '__main__':

    s=input("Enter The String : ")

    print(reverse(s))

