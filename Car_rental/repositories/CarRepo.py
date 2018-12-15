import csv
from models.Car import Car

class CarRepo:

    def __init__(self):
        self.__cars_list = []

    def add_car(self, car):
        with open("Data/cars.csv", "a+", encoding = "utf-8") as car_file:
            lp_number = car.get_lp_number()
            category = car.get_category()
            brand = car.get_brand()
            model = car.get_model()
            colour = car.get_colour()
            year = car.get_year()
            kilometers = car.get_km()
            status = car.get_status()


            fieldnames = ["Licence Plate Number", "Category", "Brand", "Model", "Colour", "Year", "Kilometers", "Status"]

            csv_writer = csv.DictWriter(car_file, fieldnames=fieldnames, lineterminator="\n")
            #Spurning með writeheader. Virðist adda header með hverri nýrri línu.
            csv_writer.writerow({"License Plate Number" : lp_number, "Category" : category, "Brand" : brand, "Model" : model, 
            "Colour" : colour, "Year" : year, "Kilometers" : kilometers, "Status" : status})

    def remove_car(self, new_value):
        self.__new_value = new_value
        with open ("data/customers.csv", "w", encoding = "utf-8") as changed_csv:
            fieldnames = ["License Plate Number", "Category", "Brand", "Model", "Colour", "Year", "Kilometers", "Status"]
            csv_writer = csv.DictWriter(changed_csv, fieldnames = fieldnames, lineterminator = "\n")
            csv_writer.writeheader()
            for line in new_value:
                csv_writer.writerow(line)
        pass


    def get_cars_list(self):
        cars_list = []
        with open ("Data/cars.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)   #Til þess að geta filterað út frá lyklum þarf að nota DictReader
            if cars_list == []:
                for line in csv_reader:
                   if line not in self.__cars_list:
                        self.__cars_list.append(line)

        return self.__cars_list

    def available_cars(self):
        available_cars_list = []
        with open("Data/cars.csv", "r") as cars_file:          
            csv_reader = csv.DictReader(cars_file)
            for car in csv_reader:
                if car["Status"] == "Available":
                    available_cars_list.append(car)
        return available_cars_list

    def unavailable_cars(self):
        unavailable_cars_list = []
        with open("Data/cars.csv", "r") as cars_file:          
            csv_reader = csv.DictReader(cars_file)
            for car in csv_reader:
                if car["Status"] == "Unavailable":
                    unavailable_cars_list.append(car)
        return unavailable_cars_list

    def change_status(self, car):
        update_list = []
    
        with open("Data\cars.csv", "r", encoding = "utf-8") as cars_file:
            csv_reader = csv.reader(cars_file)
            
            for row in csv_reader:
                if row[0] == car.get_lp_number():
                    
                    change_row = row
                    if change_row[7] == "Taken":
                        change_row[7] = "Available"               
                    else:
                        change_row[7] = "Taken"
                    update_list.append(change_row)
            
                else:
                    update_list.append(row)
        
        with open('data/cars.csv', 'w', encoding = "utf-8") as cars_file:
            csv_writer = csv.writer(cars_file, lineterminator = "\n")
            for car in update_list:
                csv_writer.writerow(car)

