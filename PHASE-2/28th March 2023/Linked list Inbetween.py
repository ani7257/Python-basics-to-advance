#Linked list for insert end
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None

#Function to inbetween newnode
    def Inbetween(self,middle_node,newdata):
        NewNode=Node(newdata)#5000
        if middle_node is None:
            print("The mentioned node is present")
            return

        NewNode=Node(newdata)#6000
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode

#Print the linked list
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Thurs")
list.headval.nextval=e2
e2.nextval=e3
list.Inbetween(list.headval.nextval,"Wed")
list.listprint()
    
