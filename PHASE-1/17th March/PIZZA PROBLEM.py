#Practice2(Pizza Problem)
types=['small','medium','Small','Medium']
class Customer:
    def __init__(self,c_name,quantity):
        self.__c_name=c_name.title()
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    def get_c_name(self):
        return self.__c_name
    def get_quantity(self):
        return self.__quantity
class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__s_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
            if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
                if self.__pizza_type.title()=="Small":
                    self.pizza_cost=150*Customer.get_quantity(self.__customer)
                    if self.__additional_topping:
                        self.pizza_cost+=35*Customer.get_quantity(self.__customer)
                if self.__pizza_type.title()=="Medium":
                    self.pizza_cost=200*Customer.get_quantity(self.__customer)
                    if self.__additional_topping:
                        self.pizza_cost+=50*Customer.get_quantity(self.__customer)
                if not self.__s_id:
                    self.__s_id=self.__pizza_type[0]+ str(Pizzaservice.counter)
                    Pizzaservice.counter+=1
            else:
                self.pizza_cost=-1
    def get_s_id(self):
        return self.__s_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance):
        self.__delivery_charge=0
        self.__distance=distance 
        Pizzaservice.__init__(self,customer,pizza_type,additional_topping)
    def validate_distance(self):
        if self.__distance in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                dis=1
                while(dis<=self.__distance):
                    if dis in range(1,6):
                        self.pizza_cost+=5
                    if dis in range(6,11):
                        self.pizza_cost+=7
                    dis+=1
        else:
            self.pizza_cost=-1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance(self):
        return self.__distance
c=Customer("ANIKET",5)
p1=Pizzaservice(c,"MEDIUM",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_s_id())
d1=Doordelivery(c,"MEDIUM",True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_s_id())     
