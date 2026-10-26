import sys

class Stack:
    def __init__(self, size):
        self.stackSize = size
        self.myStack = []

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.myStack) == 0:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print("Stack is full. Cannot push", data)
        else:
            self.myStack.append(data)
            print(data, "pushed to stack")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop.")
        else:
            popped_value = self.myStack.pop()
            print(popped_value, "popped from stack")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Cannot peek.")
        else:
            print("Top element is:", self.myStack[-1])

    def deleteStack(self):
        self.myStack = []
        print("Stack deleted.")

    def displayStack(self):
        if self.isEmpty():
            print("Stack is empty. Nothing to display.")
        else:
            print("Stack elements are:", self.myStack)

    def getMaxElement(self):
        if self.isEmpty():
            print("Stack is empty. No max element.")
            return None
        else:
            max_element = max(self.myStack)
            return max_element

    def __str__(self):
        return "Stack size: {}, Stack elements: {}".format(
            self.stackSize, self.myStack
        )


size = int(input("Enter the size of the stack: "))
obj = Stack(size)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. isEmpty")
    print("5. isFull")
    print("6. Get max element")
    print("7. Delete Stack")
    print("8. Display Stack")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to push in the stack: "))
        obj.push(value)

    elif choice == 2:
        obj.pop()

    elif choice == 3:
        obj.peek()

    elif choice == 4:
        if obj.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")

    elif choice == 5:
        if obj.isFull():
            print("Stack is full.")
        else:
            print("Stack is not full.")

    elif choice == 6:
        print("Max element in the stack is:", obj.getMaxElement())

    elif choice == 7:
        obj.deleteStack()

    elif choice == 8:
        obj.displayStack()

    elif choice == 9:
        sys.exit()

    else:
        print("Invalid choice. Please try again.")