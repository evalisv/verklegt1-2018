from repositories.CarRepo import CarRepository

class CarService():
    def __init__(self):
        self.__car_repo = CarRepository()

    def add_car(self, car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)
    
    def is_valid_car(self, car):
        #here should be some code to 
        #validate the car
        return True

    def get_cars_list(self):
        print("{:<15} {:<15} {:<15} {:<15}".format("LP Number", "Model", "Kilometers", "Status"))
        for line in self.__car_repo.get_cars_list():
            print("{:<15} {:<15} {:<15} {:<15}".format(line["License Plate Number"], line["Model"], line["Kilometers"], line["Status"]))
        return

    def get_cars_by_status(self, status):
        pass


    def available_cars(self):
        print("{:<15} {:<15} {:<15} {:<15}".format("LP Number", "Model", "Kilometers", "Status"))
        for line in self.__car_repo.available_cars():
            print("{:<15} {:<15} {:<15} {:<15}".format(line["License Plate Number"], line["Model"], line["Kilometers"], line["Status"]))
        return

    def unavailable_cars(self):
        print("{:<15} {:<15} {:<15} {:<15}".format("LP Number", "Model", "Kilometers", "Status"))
        for line in self.__car_repo.unavailable_cars():
            print("{:<15} {:<15} {:<15} {:<15}".format(line["License Plate Number"], line["Model"], line["Kilometers"], line["Status"]))
        if self.__car_repo.unavailable_cars() == []:
            print("")
            print("")
            print("There are no available cars")
        return