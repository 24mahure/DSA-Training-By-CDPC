class Node:
    def __init__(self, value):
        #every node will contain data and a pointer to the next node
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linkedListObj=LinkedList()
# crate seprate nodes/memory
linkedListObj.head=Node(10)
secondNode=Node(20)
thirdNode=Node(30)
fourthNode=Node(40)
fithNode=Node(50)

#connecting nodes
linkedListObj.head.next=secondNode
secondNode.next=thirdNode
thirdNode.next=fourthNode
fourthNode.next=fithNode

#display linked list
while linkedListObj.head != None:
    print("|",linkedListObj.head.data,"|",end="->")
    linkedListObj.head=linkedListObj.head.next