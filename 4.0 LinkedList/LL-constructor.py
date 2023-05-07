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
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1 
        return True


    def popFirst(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index<0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        #return temp.value #required if code need a value in output

    def set(self, index, new_value):
        if self.get(index):
            self.get(index).value = new_value
            return True
        return False


myLinkedList = LinkedList(1)
myLinkedList.appendList(2)
myLinkedList.appendList(3)
myLinkedList.prepend(4)
myLinkedList.prepend(5)


print("List",myLinkedList.printList())

print(myLinkedList.get(2))
print(myLinkedList.set(0,8))
print("List",myLinkedList.printList())

# print("Pop",myLinkedList.pop())
# print("Pop",myLinkedList.pop())
# print("Pop",myLinkedList.pop())
# myLinkedList.popFirst()
# print("List",myLinkedList.printList())

        