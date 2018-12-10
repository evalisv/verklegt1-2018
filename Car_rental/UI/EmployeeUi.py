import csv
import os
from models.Customer import Customer
from models.Car import Car
from models.Order import Order
from Services.CarService import CarService
from Services.CustomerService import CustomerService
# from Services.OrderService import OrderService


class EmployeeUi:

    def __init__(self):
        self.__car_service = CarService()
        self.__customer_service = CustomerService()
        #self.__order_service = OrderService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("You can do the following:")
            print()
            print("1 | Cars")
            print("2 | Orders")
            print("3 | Customers")
            print("q | Quit")
            print()

            action = input("Input number/letter: ").lower()

            if action == "1":
                # Goes to Cars menu
                os.system("cls")
                action = ""
                while(action != "q"):    
                    print("You can do the following:")
                    print()
                    print("1 | See Available cars")
                    print("2 | See Unavailable cars")
                    print("3 | List of all cars")
                    print("4 | See Details of a car")
                    print("5 | Register new car")
                    print("m | Go to Main menu")
                    print("q | Quit")
                    print()
                    
                    action = input("Input number/letter: ").lower()
                    
                    if action == "1":
                        # See available cars
                        with open ("Data/cars.csv", "r") as csv_file:
                            csv_reader = csv.DictReader(csv_file)   #Til þess að geta filterað út frá lyklum þarf að nota DictReader

                            for line in csv_reader:
                                # Prentar aðeins út gildin sem eru tengd við þá lykla sem settir eru i hornklofana.
                                # Dæmi: print(line["Name"], "\t", line["Email"], "\t", line["Phone"])
                                # "\t" er fyrir tabs
                                print(line['Licence Plate Number'], "\t", line['Category'], "\t", line['Model'], "\t", line['Kilometers'], "\t", line['Status'])
                        print()   
                        break
                    
                    
                    if action == "2":
                        # See unavailable cars
                        pass
                    
                    
                    if action == "3":
                        # List of all cars
                        pass

                    
                    if action == "4":
                        # See details of a car
                        pass

                    
                    if action == "m":
                        # Go to Main menu
                        break
            
                    if action == "5":
                        # Register new car
                        os.system("cls")
                        lp_number = input("Licence plate number: ")
                        category = input("Category: ")
                        model = input("Model: ")
                        brand = input("Brand: ")
                        colour = input("Colour: ")
                        year = input("Year: ")
                        kilometers = input("Kilometers: ")
                        status = input("Status: ")
                        new_car = Car(lp_number, category, model, brand, colour, year, kilometers, status)
                        self.__car_service.add_car(new_car)
                        
                                        

            if action == "2":
                # Goes to Orders menu
                pass

            if action == "3":
                # Goes to Customers menu
                os.system("cls")
                action = ""
                while(action != "q"):
                    print("You can do the following:")
                    print()
                    print("1 | Register new customer")
                    print("2 | List all customers")
                    print("3 | Change customer information")
                    print("4 | Remove customer from system")
                    print("m | Go to Main menu")
                    print("q | Quit")
                    print()

                    action = input("Input number/letter: ").lower()
                    
                    
                    if action == "1":
                        # Register new customer
                        os.system("cls")
                        id_number = input("Customer ID: ")
                        name = input("Name: ")
                        age = input("Age: ")
                        country = input("Country: ")
                        email = input("E-mail: ")
                        phone = input("Phone number: ")
                        dl_number = input("Drivers license number: ")
                        cc_number = input("Credit card number: ")
                        new_customer = Customer(id_number, name, age, country, email, phone, dl_number, cc_number)
                        self.__customer_service.add_customer(new_customer)
                        os.system("cls")
                        break

                    
                    if action == "":
                        pass

                    
                    if action == "":
                        pass

                    
                    if action == "":
                        pass

                    
                    if action == "m":
                        # Go to Main menu
                        break
                        


                    
            
