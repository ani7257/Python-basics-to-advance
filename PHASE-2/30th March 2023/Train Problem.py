#Implement the class Train
class Compartment:
    def __init__(self, name, capacity, num_passengers):
        self.name = name
        self.capacity = capacity
        self.num_passengers = num_passengers

class Train:
    def __init__(self, train_name, compartment_list):
        self.train_name = train_name
        self.compartment_list = compartment_list
        
    def get_train_name(self):
        return self.train_name
    
    def get_compartment_list(self):
        return self.compartment_list
    
    def count_compartments(self):
        return len(self.compartment_list)
    
    def check_vacancy(self):
        count = 0
        for compartment in self.compartment_list:
            if compartment.num_passengers < compartment.capacity/2:
                count += 1
        return count
        
