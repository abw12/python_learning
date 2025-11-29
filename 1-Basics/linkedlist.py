class Node:
    def __init__(self,data):
        self.data=data
        self.next=None ##pointer


## 1->2->3->None

class LinkedList:

    def __init__(self):
        self.head=None

    ## insert a value into linkedlist
    def insert(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node
    
    def update(self,value,index):
        current_node = self.head
        position=0
        if position == index:
            current_node.data = value
        else:
            while(current_node != None and position!=index):
                position+=1
                current_node=current_node.next
            
            if current_node != None:
                current_node.data = value
            else:
                print("Index not present")
    
 
    def printLL(self):
        current_node = self.head
        while(current_node != None):
            print(current_node.data)
            current_node=current_node.next

 


# create a new linked list
llist = LinkedList()
llist.insert(7)
llist.insert(10)
llist.insert(19)
llist.printLL()      
llist.update(23,2)
llist.printLL() 
