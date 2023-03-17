#Practice9
'''class Book:
    def __init__(self):
        self.title=None
my_fav=Book()#1000
your_fav=Book()
my_fav.title="Head First Programming"
your_fav.title="Learn Python the hard way"

my_fav.title="Learning Python"
print("My favourite is",my_fav.title)
print("Your's is",your_fav.title)'''

#Practice10
'''class Shoe:
    def __init__(self, price, material):
        self.price=price
        self.material=material

s1=Shoe(1000,"Camvas")
print("The unique id of the object",id(s1))'''

#Practice11
'''class Shoe:
    def __init__(self, price, material):
        self.price=price
        self.material=material

    def __str__(self):
        return "Shoe with price:"+str(self.price)+"and material:"+self.material

s1=Shoe(1000,"Camvas")
print(s1)'''


#Practice12
'''class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")

    def purchase(self):
        self.display()
        print("Calculating price")

#Mobile().purchase()
#Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2#m1=200
print(m1)#200
print(m2)#200'''

#Practice13
'''class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print("Total price of",self.brand,"mobile is",self.total_price)
    def amount_returned(self):
        return (self.price-self.total_price)
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())'''

#Practice14
'''class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.wallet_balance+=amount
    def show_balance(self):
        print("The balance is",self.wallet_balance)
c1=Customer(100,"Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()'''

#Practice15
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def set_balance(self,amount):
        if amount<50000 and amount>0:
            self.__wallet_balance+=amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Gopal",24,1000)
print(c1.get_wallet_balance())
#print(c1.__wallet_balance)
c1.set_balance(5000)
print(c1.get_wallet_balance())

#Practice16
'''class Table:
    def __init__self():
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)'''


