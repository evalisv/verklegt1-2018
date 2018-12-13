from repositories.CarRepo import CarRepo

class CarService():
    def __init__(self):
        self.__car_repo = CarRepo()

    def add_car(self, car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)
    
    def is_valid_car(self, car):
        #here should be some code to 
        #validate the car
        return True

    def get_cars_list(self):
        print()
        print("List of all cars")
        print()
        print(" ", "{:<15} {:<15} {:<15} {:<15}".format("LP Number", "Model", "Kilometers", "Status"))
        print("-"*60)
        for line in self.__car_repo.get_cars_list():
            print(" ","{:<15} {:<15} {:<15} {:<15}".format(line["License Plate Number"], line["Model"], line["Kilometers"], line["Status"]))
        return

    def get_cars_by_status(self, status):
        pass


    def available_cars(self):
        print()
        print("List of available cars")
        print()
        print(" ","{:<15} {:<15} {:<15} {:<15}".format("LP Number", "Model", "Kilometers", "Status"))
        print("-"*60)
        for line in self.__car_repo.available_cars():
            print("","{:<15} {:<15} {:<15} {:<15}".format(line["License Plate Number"], line["Model"], line["Kilometers"], line["Status"]))
        if self.__car_repo.available_cars() == []:
            print("")
            print("")
            print(" There are no available cars")
        return

    def unavailable_cars(self):
        print()
        print("List of unavailable cars")
        print()
        print(" ","{:<15} {:<15} {:<15} {:<15}".format("LP Number", "Model", "Kilometers", "Status"))
        print("-"*60)
        for line in self.__car_repo.unavailable_cars():
            print(" ","{:<15} {:<15} {:<15} {:<15}".format(line["License Plate Number"], line["Model"], line["Kilometers"], line["Status"]))
        if self.__car_repo.unavailable_cars() == []:
            print(" ")
            print(" ")
            print(" There are no unavailable cars")
        return
