#Practice1
'''class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, cost):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__cost = cost
        self.__premium_amount = 0

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium(self):
        if self.__vehicle_type == "Two wheeler":
            self.__premium_amount = self.__cost * 0.02
        elif self.__vehicle_type == "Four wheeler":
            self.__premium_amount = self.__cost * 0.06
        else:
            print("Invalid vehicle type")

    def display_vehicle_details(self):
        print("Vehicle ID:", self.__vehicle_id)
        print("Vehicle type:", self.__vehicle_type)
        print("Vehicle cost:", self.__cost)
        print("Premium amount:", self.__premium_amount)


vehicle1=Vehicle("B008", "Two wheeler", 730000)
vehicle2=Vehicle("D008", "Four wheeler", 100000)

vehicle1.calculate_premium()
vehicle1.display_vehicle_details()

vehicle2.calculate_premium()
vehicle2.display_vehicle_details()

vehicle1.set_cost(80000)
vehicle2.set_cost(200000)

vehicle1.calculate_premium()
vehicle2.calculate_premium()
vehicle1.display_vehicle_details()
vehicle2.display_vehicle_details()'''

#Practice2
'''class Student:
    def __init(self):
        self.__sid = None
        self.__age = None
        self.__mark = None
    def validate_marks(self):
        if self.__mark<=100 and self.__mark>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualifications(self):
        if self.validate_age() and self.validate_marks() and self.__mark>=65:
            return True
        else:
            return False
    def discount_applicable(self):
        if self.check_qualifications() and self.__mark>85:
            print("25% Discount Applicable")
        else:
            print("No discount applicable")
    def get_sid(self):
        return self.__sid
    def get_age(self):
        return self.__age
    def get_mark(self):
        return self.__mark
    def set_sid(self,sid):
        self.__sid=sid
    def set_age(self,age):
        self.__age=age
    def set_mark(self,mark):
        self.__mark=mark
s1 = Student()
s1.set_sid(186)
s1.set_age(22)
s1.set_mark(89)
s1.check_qualifications()
s1.discount_applicable()
s1.set_mark(50) 
print(s1.check_qualifications())
s1.discount_applicable()'''

#Practice3
class Customer:
    def validate_quantity(self, quantity):
        if 1 <= quantity <= 5:
            return True
        else:
            return False


class Pizzaservice:
    counter = 100
    
    def __init__(self, pizza_type, quantity, additional_topping):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.pizza_cost = 0
        self.service_id = ''
    
    def validate_pizza_type(self):
        if self.pizza_type.lower() == 'small' or self.pizza_type.lower() == 'medium':
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            if self.pizza_type.lower()=='small':
                self.pizza_cost=self.quantity*150
                if self.additional_topping:
                    self.pizza_cost+=self.quantity*35
            else:
                self.pizza_cost=self.quantity*200
                if self.additional_topping:
                    self.pizza_cost+=self.quantity*50
            
            Pizzaservice.counter+=1
            self.service_id=self.pizza_type[0].upper()+str(Pizzaservice.counter)
        else:
            self.pizza_cost=-1


class Doordelivery(Pizzaservice):
    def __init__(self, pizza_type, quantity, additional_topping, distance_in_kms):
        super().__init__(pizza_type, quantity, additional_topping)
        self.distance_in_kms=distance_in_kms
    
    def validate_distance_in_kms(self):
        if 1<=self.distance_in_kms<=10:
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost!=-1:
                if self.distance_in_kms<=5:
                    self.pizza_cost+=self.distance_in_kms*5
                else:
                    self.pizza_cost+=5*5+(self.distance_in_kms-5)*7
        else:
            self.pizza_cost = -1




