#Functions
'''def function1():
    print("Its a function")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
    #print()__str__
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function3(100,200))
def function4(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function4(10,20.2))
def function5(num1,num2):
    num3=float(num1)+num2
    return num3
print("value returned",function5('10',20.2))'''

#categories of functions
#based on arguments
#positional arguments
#data is allocated from right to left
'''def fun6(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun6(10,20,30,40)
fun6(10,20,30,400)
fun6(10,20,30,450)'''

#2 keyword arguments
'''def fun7(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun6(num4=10,num3=20,num2=30,num1=40)'''

#3 default arguments
'''def function3(name,rollno,branch="CSE",collegename="GIETU"):
    print(name,rollno,branch,collegename)
function3("Aniket","44")
function3("Barsha","40")
function3("Neeraj","54","CST")
function3("Piyush","38","ECE")'''

#4 :variable no. of arguments

'''def function4(*var): #var is tuple
    for i in var:
        print(i,end=' ')
        
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)'''

#Example1
'''def add(*var): #var is tuple
    sum1=0
    for i in var:
        sum1=sum1+i
    print(sum1)
add(10,20)
print()
add(10,20,30,40)
print()
add(10,20,30,40,50,60)'''

#Example2
'''def add(*var): #var is tuple
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print()
print(add(10,20,30,40))
print()
print(add(10,20,30,40,50,60))
print()'''



