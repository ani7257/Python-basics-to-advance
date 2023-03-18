#Practice1(To find the premium of vehicles for two types are two wheelers and four wheelers)
class Vehicle:
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
vehicle2.display_vehicle_details()
