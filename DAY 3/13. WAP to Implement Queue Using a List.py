class Queue:
    def __init__(self, size):
        self.queueSize = size
        self.myqueue = []

    def isFull(self):
        if len(self.myqueue) == self.queueSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.myqueue == []:
            return True
        else:
            return False

    def enQueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            self.myqueue.append(data)
            print("Enqueued:", data)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            data = self.myqueue.pop(0)
            print("Dequeued:", data)

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("First element:", self.myqueue[0])

    def deleteQueue(self):
        self.myqueue = []
        print("Queue deleted")

    def displayQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.myqueue)


size = int(input("Enter the size of the queue: "))

obj = Queue(size)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek Front Element")
    print("4. Display Queue")
    print("5. Delete Queue")
    print("6. Check if Queue is Full")
    print("7. Check if Queue is Empty")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter the element to enqueue: ")
        obj.enQueue(data)

    elif choice == '2':
        obj.deQueue()

    elif choice == '3':
        obj.peek()

    elif choice == '4':
        obj.displayQueue()

    elif choice == '5':
        obj.deleteQueue()

    elif choice == '6':
        if obj.isFull():
            print("Queue is full")
        else:
            print("Queue is not full")

    elif choice == '7':
        if obj.isEmpty():
            print("Queue is empty")
        else:
            print("Queue is not empty")

    elif choice == '8':
        break

    else:
        print("Invalid choice. Please try again.")