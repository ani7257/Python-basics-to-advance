class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        c=0
        while temp is not None:
            temp=temp.next
            c+=1
        return c
    def insertatbeginning(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous==new_node
            self.head=new_node
    def insertatend(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertatbeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.previous=temp
    def insertatposition(self,value,position):
        temp=self.head
        c=0
        while temp is not None:
            if c==position-1:
                break
            c+=1
            temp=temp.next
            if position==1:
                self.insertatbeginning(value)
            elif temp is None:
                print("There are less than {} -1 elements in the  ")
            elif temp.next is None:
                self.insertatend(value)
            else:
                new_node=Node(value)
                new_node.next=temp.next
                new_node.previous=temp
                temp.next.previous=new_node
                temp.next=new_node
   
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=' ')
            temp=temp.next
x=DoublyLinkedList()
print(x.isEmpty())
x.insertatend(5)
x.insertatend(15)
x.insertatend(25)
x.insertatend(35)
x.insertatend(45)
x.printlist()
x.insertatbeginning(50)
print("After inserting")
x.printlist()
print("No of nodes",x.length())
print("Insert at position 2 number 8")
x.insertatposition(8,2)
x.printlist()
