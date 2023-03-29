#Traversing a Linked List
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

list=SLinkedList()
list.headval=Node("Mon")#1000
e2=Node("Tue")#2000
e3=Node("Wed")#3000

#Link first Node to second node
list.headval.nextval=e2

#Link second Node to third node
e2.nextval=e3
list.listprint()
