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
    
    #POP Element at end of list
    def pop(self):
        #for empty list
        if self.length == 0:
            return None
        
        #2 new variables declared
        temp = self.head
        pre = self.head
        
        #traversing pointers to end of list
        while(temp.next):
            pre = temp
            temp = temp.next
        
        #popping the last node by swapping the values.
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        #if tail and head both are null length after popping.
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp.value
        






myLinkedList = LinkedList(1)
myLinkedList.appendList(2)
myLinkedList.appendList(3)

print("List",myLinkedList.printList())

print("Pop",myLinkedList.pop())
print("Pop",myLinkedList.pop())
print("Pop",myLinkedList.pop())
print("List",myLinkedList.printList())
        
    #def append(self, value):
        #create new node at the end

    #def prepend(self, value):
        #create new node at the head

    #def insert(self, value, index):
        #create a node at an index in between the list