class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        ref=self.head
        while(ref is not None):
            print(ref.data)
            ref=ref.next
   
   
   
llist=LinkedList()
print("Given Linked List")
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.printlist()
llist.reverse()
print("Reverse Linked List")
llist.printlist()
