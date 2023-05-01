class Node:
    #create new node
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        NewNode = Node(value)
        self.head = NewNode
        self.tail = NewNode
        self.length = 1
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def appendList(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True
    
    def pop(self):
        if self.length == 0:
            return None
        while(temp.next):
            pre = temp
            temp = temp.next
        temp = self.head
        pre = self.head






myLinkedList = LinkedList(4)
myLinkedList.appendList(2)

print(myLinkedList.printList())
        
    #def append(self, value):
        #create new node at the end

    #def prepend(self, value):
        #create new node at the head

    #def insert(self, value, index):
        #create a node at an index in between the list