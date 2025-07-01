"""
Paul Deater
Paul_Deater_M3_Lab
This takes in information about a vehicle and then prints that information out to the user in clean and easy to read format
"""

class Vehicle:
    # variables
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    # getter
    def get_vehicle_type(self):
        return self.vehicle_type
    
    # setter
    def set_vehicle_type(self,incoming_value):
        self.vehicle_type = incoming_value
    
class Automobile(Vehicle):
    # variables
    def __init__(self, year, vehicle_type, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # getters
    def get_year(self):
        return self.year
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_doors(self):
        return self.doors
    def get_roof(self):
        return self.roof
    
    # setters
    def set_year(self,incoming_value):
        self.year = incoming_value
    def set_make(self,incoming_value):
        self.make = incoming_value
    def set_model(self,incoming_value):
        self.model = incoming_value
    def set_doors(self,incoming_value):
        self.doors = incoming_value
    def set_roof(self,incoming_value):
        self.roof = incoming_value


def main():
    # class shorthands
    vehicle = Vehicle("")
    automobile = Automobile("","","","","","")

    user_vehicle_type = input("Please enter vehicle type: ")
    vehicle.set_vehicle_type(user_vehicle_type)
    
    # gets inputs
    user_year = input("Please enter year: ")
    user_make = input("Please enter the make: ")
    user_model = input("Please enter the model: ")
    user_doors = input("Please enter the number of doors: ")
    user_roof = input("Please enter type of roof: ")
    
    # sets the incoming inputs
    automobile.set_year(user_year)
    automobile.set_make(user_make)
    automobile.set_model(user_model)
    automobile.set_doors(user_doors)
    automobile.set_roof(user_roof)
    
    # retreives the data
    retrieve_user_vehicle_type = vehicle.get_vehicle_type()
    retrieve_user_year = automobile.get_year()
    retrieve_user_make = automobile.get_make()
    retrieve_user_model = automobile.get_model()
    retrieve_user_doors = automobile.get_doors()
    retrieve_user_roof = automobile.get_roof()

    # prints the data
    print("Vehicle type: ",retrieve_user_vehicle_type)
    print("Year: ", retrieve_user_year)
    print("Make: ", retrieve_user_make)
    print("Model:", retrieve_user_model)
    print("Number of doors", retrieve_user_doors)
    print("Type of roof:", retrieve_user_roof)



main()
