'''
a teacher has given a project assignment to a class of 10 students.
she wants to store the marks (out of 100) scored by each student.the marks scored are as mentioned below:
89,78,99,76,77,67,99,98,90
write a python program to store the marks in a list and perform the following:
    1.the teacher forgot to include the marks of one student.Insert 78 at index position, 8 and display the marks of all 10 students.
    2.the teacher also wants to know the scored  by students represented by index position, 5 and 7.identify and display the two marks.
    '''
class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class student:
    def __init__(self):
        self.headval=None
       
    # trversal of linked list
    def listprint(self):
        printval=self.headval
        while printval is   not None:
            print(printval.dataval)
            printval=printval.nextval
           
    def insert_value_by_index(self,index,data):
        if index==1:
            new_node=node(data)
            new_node.nextval=self.headval
            self.headval=new_node
        i=1
        n=self.headval
        while i<index-1 and n is not None:
            n=n.nextval
            i+=1
        if n is None:
            print("index out of bound")
        else:
            new_node=node(data)
            new_node.nextval=n.nextval
            n.nextval=new_node
    def search(self,index):
        if index==1:
            print(self.headval.dataval)
        i=1
        n=self.headval
        while i<index-1 and n is not None:
            n=n.nextval
            i+=1
        if n is None:
            print("index out of bound")
        else:
            print(n.nextval.dataval)
       
       
           
list1=student()
list1.headval=node(89)
e2=node(78)
e3=node(99)
e4=node(76)
e5=node(77)
e6=node(67)
e7=node(99)
e8=node(98)
e9=node(90)
list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=e9
list1.insert_value_by_index(8,78)
list1.listprint()
print()
list1.search(5)
print()
list1.search(7)
