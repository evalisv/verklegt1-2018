import csv
from models.Car import Car

class CarRepository:

    def __init__(self):
        self.__car = []

    def add_car(self, car):
        with open('Car_rental\Data\car.csv', 'a+') as car_file:
            lp_number = car.get_lp_number()
            category = car.get_category()
            model = car.get_model()
            brand = car.get_brand()
            colour = car.get_colour()
            year = car.get_year()
            kilometers = car.get_km()
            status = car.get_status()


            fieldnames = ['Licence plate', 'Category', 'Model', 'Brand', 'Colour', 'Year', 'kilometers', 'status']

            csv_writer = csv.DictWriter(car_file, fieldnames=fieldnames, lineterminator = "\n")
            #Spurning með writeheader. Virðist adda header með hverri nýrri línu.
            csv_writer.writeheader()
            csv_writer.writerow({'Licence plate' : lp_number, 'Category' : category, 'Model' : model, 'Brand' : brand,
             'Colour' : colour, 'Year' : year, 'kilometers' : kilometers, 'status' : status})
