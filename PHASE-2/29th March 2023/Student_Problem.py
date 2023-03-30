#question

class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class student:
    def __init__(self):
        self.headval=None
       
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval,end='')
            printval=printval.nextval
   
    def delete_value(self,data):
        if self.headval is None:
            print("no node to delete")
            return
        if self.headval.dataval==data:
            self.headval=self.headval.nextval
            return
        n=self.headval
        while(n.nextval is not None):
            if n.nextval.dataval==data:
                break
            n=n.nextval
        if n.nextval is None:
            print(" item not found")
        else:
            n.nextval=n.nextval.nextval
                   
def new_list(list1):
        l1=[]
        if list1.headval is None:
            print(" no element in list")
        if list1.headval.nextval is None:
            l1.append(list1.head.dataval)
            return
        n=list1.headval
        while n.nextval is not None:
            l1.append(n.nextval.dataval)
            n=n.nextval
       
        for i in range(len(l1)):
            if( l1[i]=='*' or l1[i]=='/'):
                l1[i]=' '
            elif l1[i-1]==' ' and l1[i-2]==' ':
                print('hi')
                l1[i-1]=''
                l1[i]=l1[i].upper()
            else:
                continue
        for i in l1:
            print(i,end='')        
                   
list1=student()
list1.headval=node('A')
e2=node('n')
e3=node('*')
e4=node('/')
e5=node('a')
e6=node('p')
e7=node('p')
e8=node('l')
e9=node('e')
e10=node('*')
e11=node('a')
e12=node('/')
e13=node('day')
e14=node('*')
e15=node('*')
e16=node('k')
e17=node('e')
e18=node('e')
e19=node('p')
e20=node('s')
e21=node('/')
e22=node('*')
e23=node('a')
e24=node('/')
e25=node('/')
e26=node('d')
e27=node('o')
e28=node('c')
e29=node('t')
e30=node('o')
e31=node('r')
e32=node('*')
e33=node('A')
e34=node('w')
e35=node('a')
e36=node('y')
list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=e9
e9.nextval=e10
e10.nextval=e11
e11.nextval=e12
e12.nextval=e13
e13.nextval=e14
e14.nextval=e15
e15.nextval=e16
e16.nextval=e17
e17.nextval=e18
e18.nextval=e19
e19.nextval=e20
e20.nextval=e21
e21.nextval=e22
e22.nextval=e23
e23.nextval=e24
e24.nextval=e25
e25.nextval=e26
e26.nextval=e27
e27.nextval=e28
e28.nextval=e29
e29.nextval=e30
e30.nextval=e31
e31.nextval=e32
e32.nextval=e33
e33.nextval=e34
e34.nextval=e35
e35.nextval=e36
new_list(list1)

