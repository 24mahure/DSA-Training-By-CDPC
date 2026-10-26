class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            popped_value = self.top.data
            self.top = self.top.next
            print(popped_value, "popped from stack")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        current = self.top

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.peek()

stack.pop()

stack.display()