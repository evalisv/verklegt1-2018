import csv
from models.Car import Car

class CarRepository:

    def __init__(self):
        self.__car = []

    def add_car(self, car):
        with open('Data/cars.csv', 'a+', encoding = "utf-8") as car_file:
            lp_number = car.get_lp_number()
            category = car.get_category()
            model = car.get_model()
            brand = car.get_brand()
            colour = car.get_colour()
            year = car.get_year()
            kilometers = car.get_km()
            status = car.get_status()


            fieldnames = ['Licence Plate Number', 'Category', 'Model', 'Brand', 'Colour', 'Year', 'Kilometers', 'Status']

            csv_writer = csv.DictWriter(car_file, fieldnames=fieldnames, lineterminator="\n")
            #Spurning með writeheader. Virðist adda header með hverri nýrri línu.
            csv_writer.writerow({'Licence Plate Number' : lp_number, 'Category' : category, 'Model' : model, 'Brand' : brand,
             'Colour' : colour, 'Year' : year, 'Kilometers' : kilometers, 'Status' : status})

    def get_car(self):
        return self.__car

    def available_cars():
        with open('cars.csv', 'r', encoding = "utf-8", lineterminator = "\n") as cars_file:
            available_cars_list = []
            csv_reader = csv.reader(cars_file)
            for car in cars_file:
                if car[7] == 'Available':
                    available_cars_list.append(car)
        return available_cars_list

    def change_status(self, car):
        
        update_list = []
    
        with open('cars.csv', 'r', encoding = "utf-8", lineterminator = "\n") as cars_file:
            csv_reader = csv.reader(cars_file)
            
            for row in csv_reader:
                if row[0] == car.get_liscence():
                    change_row = row
                    if change_row[7] == 'Taken':
                        change_row[7] = 'Available'               
                    else:
                        change_row[7] = 'Taken'
                    update_list.append(change_row)
            
                else:
                    update_list.append(row)
        
        with open('cars.csv', 'w', newline='') as cars_file:
            csv_writer = csv.writer(cars_file)
            for car in update_list:
                csv_writer.writerow(car)

