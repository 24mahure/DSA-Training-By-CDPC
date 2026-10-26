class Node:
   def __init__(self, value):
        #every node will contain data and a pointer to the next node
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # head is going to represent the starting node 
        self.tail = None  # tail is going to represent the end node 

# add node in the end
    def addNodeEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def display(self):
        current = self.head
        while current is not None:
            print("|", current.data, "|", end="->")
            current = current.next
        print("None")  # Indicate the end of the linked list

linkedListObj = LinkedList()
linkedListObj.addNodeEnd(10)
linkedListObj.addNodeEnd(20)
linkedListObj.addNodeEnd(30)
linkedListObj.display()