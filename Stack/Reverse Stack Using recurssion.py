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
        return 0

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



def insert_at_beginning(arr,item):
    if(Stack.isEmpty(ob)==-1):
        Stack.push(ob,item)
    else:
        temp=Stack.pop(ob)
        insert_at_beginning(arr,item)
        Stack.push(temp)

def reverseStack(arr):

    if not Stack.isEmpty(Stack()):
        temp=ob.pop()
        reverseStack(arr)
        insert_at_beginning(ob.arr,temp)



n=int(input("Enter Length of Stack"))
ob=Stack()

print("Input stack ele ")
for i in range(n):
    ele=int(input())
    ob.push(ele)
print(ob.display())
reverseStack(ob.arr)

print(ob.display())


