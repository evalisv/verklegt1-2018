import csv
import os
from models.Customer import Customer
from models.Car import Car
from models.Order import Order
from models.Price import Price
from Services.CarService import CarService
from Services.CustomerService import CustomerService
from Services.PriceService import PriceService
# from Services.OrderService import OrderService

indent = (" "*3)

class EmployeeUi:

    def __init__(self):
        self.__car_service = CarService()
        self.__customer_service = CustomerService()
        self.__price_service = PriceService()
        #self.__order_service = OrderService()

    def main_menu(self):
        action = ""
        while(action != "q"):
            os.system("cls")
            print(" You can do the following:")
            print(30 *"-")
            print(indent,"1 | Cars")
            print(indent,"2 | Orders")
            print(indent,"3 | Customers")
            print(indent,"q | Quit")
            print()

            action = input(" Input number/letter: ").lower()

            if action == "1":
                # Goes to Cars menu
                os.system("cls")
                action = ""
                while(action != "q"):    
                    print(" You can do the following:")
                    print(30 *"-")
                    print(indent,"1 | See Available cars")
                    print(indent,"2 | See Unavailable cars")
                    print(indent,"3 | List of all cars")
                    print(indent,"4 | See Details of a car")
                    print(indent,"5 | Register new car")
                    print(indent,"6 | Prices")
                    print(indent,"m | Go to Main menu")
                    print(indent,"q | Quit")
                    print()
                    
                    action = input(" Input number/letter: ").lower()
                    
                    if action == "1":
                        # See available cars
                        os.system("cls")
                        action = ""
                        self.__car_service.available_cars()
                        print()
                        print(indent,"m | Go to Main Menu")
                        action = input(" Input letter: ")

                        if action == "m".lower():
                            break
                    
                    
                    if action == "2":
                        # See unavailable cars
                        os.system("cls")
                        action = ""
                        self.__car_service.unavailable_cars()
                        print()
                        print(indent,"m | Go to Main Menu")
                        action = input(" Input letter: ").lower()

                        if action == "m".lower():
                            break
                    
                    
                    if action == "3":
                        # List of all cars
                        os.system("cls")
                        action = ""
                        self.__car_service.get_cars_list()
                        print()
                        print(indent,"m | Go to Main Menu")
                        action = input(" Input letter: ").lower()

                        if action == "m".lower():
                            break 

                    
                    if action == "4":
                        # See details of a car
                        pass

                    
                    if action == "m":
                        # Go to Main menu
                        break
            
                    if action == "5":
                        # Register new car
                        os.system("cls")
                        lp_number = input(" Licence plate number: ")
                        category = input(" Category: ")
                        model = input(" Model: ")
                        brand = input(" Brand: ")
                        colour = input(" Colour: ")
                        year = input(" Year: ")
                        kilometers = input(" Kilometers: ")
                        status = input(" Status: ")
                        new_car = Car(lp_number, category, model, brand, colour, year, kilometers, status)
                        self.__car_service.add_car(new_car)

                    if action == "6":
                        # See price list
                        os.sytem("cls")
                        action = ""
                        while(action != "q"):    
                            print(" You can do the following:")
                            print(30 *"-")
                            print(indent,"1 | See price list")
                            print(indent,"2 | Calculate prices")
                            print(indent,"m | Go to Main menu")
                            print(indent,"q | Quit")
                            print()

                            action = input(" Input number/letter: ").lower()

                            if action == "1":
                                self.__price_service.get_price_list()
                                print()
                                print(indent,"m | Go to Main Menu")
                                action = input(" Input number/letter: ")

                            if action == "2":
                                print( "Choose class: ")
                                print(30 *"-")
                                print(indent,"A | Class A")
                                print(indent,"B | Class B")
                                print(indent,"C | Class C")
                                print(indent,"m | Go to Main menu")
                                print(indent,"q | Quit")
                                print()
                                
                                class_filter = input(" Input letter:  ")
                                days = int(input(" Input number of days: ")
                                self.__price_service.calculate_price(class_filter,days)
                                print()
                                print(indent,"m | Go to Main Menu")
                                
                                
                    
                                        

            if action == "2":
                # Goes to Orders menu
                os.system("cls")
                action = ""
                while(action != "q"):    
                    print(" You can do the following:")
                    print(30 *"-")
                    print(indent,"1 | Rent cars") # ætti að koma valmöguleik að register new customers OR choose customers 
                    print(indent,"2 | Calculate Cost of rent")
                    print(indent,"3 | Return cars")
                    print(indent,"4 | Change Reservation")
                    print(indent,"5 | Cancel Reservation")
                    print(indent,"6 | Go Back")
                    print(indent,"m | Go to Main menu")
                    print(indent,"q | Quit")
                    print()

                    action = input(" Input number/letter: ").lower()           

                    if action == "1":
                        #Rent cars and ther under 
                        os.system("cls")
                        action = ""
                        while(action != "q"):    
                            print(" You can do the following:")
                            print(30 *"-")
                            print(indent,"1 | Register new customers")  
                            print(indent,"2 | Choose customers")
                            print(indent,"m | Go to Main menu")
                            print()

                            action = input(" Input number/letter: ").lower()
                        
                            if action == "1":
                                #Register new customers
                                pass

                            if action == "2":
                                #Choos customers
                                pass

                            if action == "m":
                                #Go to Main Menu
                                break



                    if action == "2":
                        #Calculate Cost of rent
                        pass

                    if action == "3":
                        #Return Cars
                        pass

                    if action == "4":
                        #Change Reservation
                        pass

                    if action == "5":
                        #Cancel Reservation
                        pass 

                    if action == "6":
                        #Go Back
                        pass

                    if action == "m":
                        #Go to Main Menu
                        break
                    
                    if action == "q":
                        #Quit
                        pass



            if action == "3":
                # Goes to Customers menu
                os.system("cls")
                action = ""
                while(action != "q"):
                    print(" You can do the following:")
                    print(30 *"-")
                    print(indent, "1 | Register new customer")
                    print(indent,"2 | List all customers")
                    print(indent,"3 | Change customer information")
                    print(indent,"4 | Remove customer from system")
                    print(indent,"m | Go to Main menu")
                    print(indent,"q | Quit")
                    print()

                    action = input(" Input number/letter: ").lower()
                    
                    
                    if action == "1":
                        # Register new customer
                        os.system("cls")
                        id_number = input(" Customer ID: ")
                        first_name = input(" First name: ")
                        last_name = input(" Last name: ")
                        age = input(" Age: ")
                        country = input(" Country: ")
                        email = input(" E-mail: ")
                        phone = input(" Phone number: ")
                        dl_number = input(" Drivers license number: ")
                        cc_number = input(" Credit card number: ")
                        new_customer = Customer(id_number, first_name, last_name, age, country, email, phone, dl_number, cc_number)
                        self.__customer_service.add_customer(new_customer)
                        print(" Success! Customer has been added to the system.")
                        action = ""
                        while(action != "q"):
                            print()
                            print(indent,"m | Go main menu")
                            print(indent, "q | Quit")
                            action = input(" Input letter: ").lower()
                            if action == "m":
                                break
                        

                    
                    if action == "2":
                        # List all customers
                        os.system("cls")
                        self.__customer_service.get_customers()
                        print()
                        print(indent, "m | Go to Main Menu")
                        action = input(" Input letter: ").lower()
                        if action == "m".lower():
                            break 
                        
                     
                    if action == "3":
                        # Change customer information
                        os.system("cls")
                        action = ""
                        while(action != "q"):    
                            print(" Filter based on:")
                            print(30 *"-")
                            print(indent,"1 | Customer ID") 
                            print(indent,"2 | Drivers License Number")
                            print(indent,"m | Go to Main menu")
                            print(indent,"q | quit")

                            action = input(" Input letter/number: ").lower()

                            if action == "1":
                                os.system("cls")
                                customer_filter = input("Customer ID: ")
                                key_filter = "Customer ID"
                                
                                print(" Change:")
                                print(30 *"-")
                                print(indent,"1 | Customer ID") 
                                print(indent,"2 | First name")
                                print(indent,"3 | Last name")
                                print(indent,"4 | Date of birth")
                                print(indent,"5 | Country")
                                print(indent,"6 | E-mail address")
                                print(indent,"7 | Phone number")
                                print(indent,"8 | Drivers License number")
                                print(indent,"9 | Credit card number")
                                print(indent,"m | Go to Main Menu")
                                print(indent,"q | quit")
                                action = input(" Input number/letter: ").lower()

                                if action == "1":
                                    key = "Customer ID"
                                elif action == "2":
                                    key = "First Name"
                                elif action == "3":
                                    key = "Last Name"
                                elif action == "4":
                                    key = "Age"
                                elif action == "5":
                                    key = "Country"
                                elif action == "6":
                                    key = "Email"
                                elif action == "7":
                                    key = "Phone"
                                elif action == "8":
                                    key = "Drivers License Number"
                                elif action == "9":
                                    key = "Credit Card Number"
                                elif action == "m".lower():
                                    break

                                self.__customer_service.change_customer_info(key, key_filter, customer_filter)
                        
                            elif action == "2":
                                os.system("cls")
                                key_filter = "Drivers License Number"
                                customer_filter = input("Drivers License Number: ")
                                self.__customer_service.change_customer_info(key, key_filter, customer_filter)

                            elif action == "m":
                                break


                    
                    if action == "4":
                        #Remove Customer from system
                        os.system("cls")
                        
                        print(" You are about to remove a customer from the system.")
                        print(30 *"-")
                        
                        customer_filter = input(" Enter customers ID:  ")

                        if customer_filter != []:
                            key_filter = "Customer ID"
                            self.__customer_service.remove_customer(key_filter, customer_filter)
                        print()
                        print(indent,"m | Go to Main menu")
                        #print("q | Quit")
                        
                        action = input(" Input letter: ").lower
                        if action == "m":
                            break
                        break
                                

                    
                    if action == "m":
                        # Go to Main menu
                        break
                        


                    
            
