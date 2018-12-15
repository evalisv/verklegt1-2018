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
        print(21*"-", "List of all cars",21*"-")
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
        print(18*"-","List of available cars",18*"-")
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
        print(17*"-","List of unavailable cars",17*"-")
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

    def details_of_car(self, lp_number):
        self.__lp_number = lp_number
        match_value = 1
        cars_list = self.__car_repo.get_cars_list()
        for line in cars_list:
            
            if line["License Plate Number"] == lp_number:
                match_value += 1
                break

        if match_value == 1:
            # Notify that something wasn't found
            print()
            print(" No car found. Would you like to try again?")
            try_again = input("Y/N: ").lower()
            if try_again == "y":
                return False
            else:
                return True
        

        if match_value != 1:
            print(60*"-", "Details of a car", 60*"-")
            print()
            print("You found this car:")
            print()
            print(" ","{:<30} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Licence Plate Number", "Category", "Model", "Brand", "Colour", "Year", "Kilometers", "Status"))
            print("-"*140)
            print(" ","{:<30} {:15} {:15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(line["License Plate Number"], line["Category"], line["Model"], line["Brand"], line["Colour"], line["Year"], line["Kilometers"], line["Status"]))
            return True


    def remove_car(self, key_filter, car_filter):
        self.__car_filter = car_filter
        self.__key_filter = key_filter
        match_value = 1
        cars_list = self.__car_repo.get_cars_list()
        for line in cars_list:
            
            if line[key_filter] == car_filter:
                print(" Car to be removed:", line["License Plate Number"])
                match_value += 1
                print(" Confirm removal?")
                action = input( "Y/N: ").lower()
                if action == "y":
                    cars_list.remove(line)
                if action == "n":
                    print(" Car removal canceled")
                    print(" Do you want to try again?")
                    try_again = input("Y/N: ").lower()
                    if try_again == "y":
                        return False
                    else:
                        return True
        if match_value == 1:
            # Notify that something wasn't found
            print(" No car with given license plate number found. Do you want to try again?")
            try_again = input("Y/N: ")
            if try_again == "y":
                return False
            else:
                return True
        if match_value != 1 and action =="y":
            self.__car_repo.remove_car(cars_list)
            print(" Success! Car has been removed from the system")
            return True    