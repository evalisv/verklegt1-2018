import csv
import os
from models.Customer import Customer
from models.Car import Car
from models.Order import Order
from models.Price import Price
from Services.CarService import CarService
from Services.CustomerService import CustomerService
from Services.PriceService import PriceService
from Services.OrderService import OrderService
from ui.login import login

indent = (" "*3)

class EmployeeUi:

    def __init__(self):
        self.__car_service = CarService()
        self.__customer_service = CustomerService()
        self.__price_service = PriceService()
        self.__order_service = OrderService()

    def main_menu(self):
        access = login()
        print(access)
        action = ""
        while(action != "q"):
            # os.system("cls")
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
                
                action = ""
                while(action != "q"):   
                    os.system("cls") 
                    print(" You can do the following:")
                    print(30 *"-")
                    print(indent,"1 | See Available cars")
                    print(indent,"2 | See Unavailable cars")
                    print(indent,"3 | List of all cars")
                    print(indent,"4 | See Details of a car")
                    print(indent,"5 | See price list")
                    if access == "admin":
                        print(indent,"6 | Register new car")
                        print(indent,"7 | Change price list")
                        print(indent,"8 | Change car registration")
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
                        print(indent,"b | Go back")
                        print(indent,"m | Go to Main Menu")
                        action = input(" Input letter: ")

                        if action == "m".lower():
                            break
                    
                    
                    elif action == "2":
                        # See unavailable cars
                        os.system("cls")
                        action = ""
                        self.__car_service.unavailable_cars()
                        print()
                        print(indent,"b | Go back")
                        print(indent,"m | Go to Main Menu")
                        
                        action = input(" Input letter: ").lower()

                        if action == "m".lower():
                            break
                    
                    
                    elif action == "3":
                        # List of all cars
                        os.system("cls")
                        action = ""
                        self.__car_service.get_cars_list()
                        print()
                        print(indent,"b | Go back")
                        print(indent,"m | Go to Main Menu")
                        action = input(" Input letter: ").lower()

                        if action == "m".lower():
                            break 

                    
                    elif action == "4":
                        # See details of a car
                        pass



                    elif action == "5":
                        # See price list
                        #os.sytem("cls")
                        action = ""
                        self.__price_service.get_price_list()
                        print()
                        print(indent,"b | Go back")
                        print(indent,"m | Go to Main Menu")
                        action = input(" Input letter: ").lower()
                                    
                    elif action == "6" and access == "admin":
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

                    elif action == "7" and access == "admin":
                        #Change price list 
                        pass

                    elif action == "8" and access == "admin":
                        #Change car registration
                        pass

                    elif action == "m":
                        # Go to Main menu
                        break
                    
                    elif action == "q":
                        #Quit
                        pass

            elif action == "2":
                # Goes to Orders menu
                
                action = ""
                while(action != "q"): 
                    os.system("cls")   
                    print(" You can do the following:")
                    print(30 *"-")
                    print(indent,"1 | Rent cars") # ætti að koma valmöguleik að register new customers OR choose customers 
                    print(indent,"2 | Calculate Cost of rent")
                    print(indent,"3 | Return cars")
                    print(indent,"4 | Change Reservation")
                    print(indent,"5 | Cancel Reservation")
                    print(indent,"m | Go to Main menu")
                    print(indent,"q | Quit")
                    print()

                    action = input(" Input number/letter: ").lower()           

                    if action == "1":
                        #Rent cars and ther under 
                        
                        action = ""
                        while(action != "q"):  
                            os.system("cls")  
                            print("You can do the following:")
                            print(30*"-")
                            print("1 | Register new customers")  
                            print("2 | Choose customers")
                            print("m | Go to Main menu")
                            print()

                            action = input("Input number/letter: ").lower()

                            if action == "m":
                                # Go to Main menu
                                break

                            print(" You can do the following:")
                            print(30 *"-")
                            print(indent,"1 | Register new customers")  
                            print(indent,"2 | Choose customers")
                            print(indent,"b | Go back")
                            print(indent,"m | Go to Main menu")
                            print(indent,"q | Quit")
                            print()

                            action = input(" Input number/letter: ").lower()

                        
                            if action == "1":
                                # Register new customer
                                os.system("cls")
                                id_number = input("Customer ID: ")
                                first_name = input("First name: ")
                                last_name = input("Last name: ")
                                age = input("Age: ")
                                country = input("Country: ")
                                email = input("E-mail: ")
                                phone = input("Phone number: ")
                                dl_number = input("Drivers license number: ")
                                cc_number = input("Credit card number: ")
                                new_customer = Customer(id_number, first_name, last_name, age, country, email, phone, dl_number, cc_number)
                                #new_customer = customer(id_number, first_name)
                                self.__customer_service.add_customer(new_customer)
                                
                                #######print(new_customer)
                                """
                                if action == "1":
                                    #Rent cars 
                                    os.system("cls")
                                    action = ""
                                    while(action != "q"):    
                                        print("You can do the following:")
                                        print(30*"-")
                                        print("1 | Rent Cars")  
                                        print("m | Go to Main menu")
                                        print("q | Quit")
                                        print()

                                        action = input("Input number/letter: ").lower()



                                        if action == "m":
                                            #Go to Main Menu
                                            break 
                                        """
                            if action == "2":
                                #Choos customers
                                pass

                            elif action == "b":
                                continue

                            elif action == "m":
                                #Go to Main Menu
                                self.main_menu()



                    elif action == "2":
                        #Calculate Cost of rent
                        pass

                    elif action == "3":
                        #Return Cars
                        pass

                    elif action == "4":
                        #Change Reservation
                        pass

                    elif action == "5":
                        #Cancel Reservation
                        pass 

                    elif action == "6":
                        #Go Back
                        pass

                    elif action == "m":
                        #Go to Main Menu
                        break
                    
                    elif action == "q":
                        #Quit
                        pass



            elif action == "3":
                # Goes to Customers menu
                
                action = ""
                while(action != "q" or action == "b"):
                    os.system("cls")
                    print(" You can do the following:")
                    print(30 *"-")
                    print(indent, "1 | Register new customer")
                    print(indent,"2 | List all customers")
                    print(indent,"3 | Change customer information")
                    if access == "admin":
                        print(indent,"4 | Remove customer from system")
                    print(indent,"b | Go back")
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
                            
                        action = ""
                        while(action != "q"):
                            print()
                            print(indent,"b | Go back")
                            print(indent,"m | Go main menu")
                            print(indent, "q | Quit")
                            action = input(" Input letter: ").lower()
                            if action == "m":
                                break
                        

                    
                    elif action == "2":
                        # List all customers
                        os.system("cls")
                        self.__customer_service.get_customers()
                        print()
                        print(indent, "b | Go back")
                        print(indent, "m | Go to Main Menu")
                        print(indent, "q | Quit")
                        action = input(" Input letter: ").lower()
                        if action == "m".lower():
                            break 
                        
                     
                    elif action == "3":
                        # Change customer information
                        
                        action = ""
                        while(action != "q"): 
                            os.system("cls")   
                            customer_filter = input("Customer ID: ")
                            action = ""
                            
                            key_filter = "Customer ID"
                            
                            print(" Change:")
                            print(30 *"-")
                            print(indent,"1 | First name")
                            print(indent,"2 | Last name")
                            print(indent,"3 | Date of birth")
                            print(indent,"4 | Country")
                            print(indent,"5 | E-mail address")
                            print(indent,"6 | Phone number")
                            print(indent,"7 | Drivers License number")
                            print(indent,"8 | Credit card number")
                            print(indent,"b | Go back")
                            print(indent,"m | Go to Main Menu")
                            print(indent,"q | quit")
                            action = input(" Input number/letter: ").lower()

                            
                            if action == "1":
                                key = "First Name"
                            elif action == "2":
                                key = "Last Name"
                            elif action == "3":
                                key = "Age"
                            elif action == "4":
                                key = "Country"
                            elif action == "5":
                                key = "Email"
                            elif action == "6":
                                key = "Phone"
                            elif action == "7":
                                key = "Drivers License Number"
                            elif action == "8":
                                key = "Credit Card Number"
                            elif action == "b":
                                break
                            elif action == "m":
                                self.main_menu()

                            if (action != "") and ((action != "m") or (action != "q") or (action != "b")):
                                self.__customer_service.change_customer_info(key, key_filter, customer_filter)
                            print(indent,"m | Go to Main Menu")
                            print(indent,"b | Go back")
                            print(indent,"q | Quit")

                            action = input("Input letter: ")
                            if action == "m":
                                break 
                            elif action == "q":
                                break
                            elif action == "b":
                                continue                 
       
                    elif action == "4" and access == "admin":
                        #Remove Customer from system
                        action = ""
                        while(action != "q"):
                            os.system("cls")
                            
                            print(" You are about to remove a customer from the system.")
                            print(30 *"-")
                            
                            customer_filter = input(" Enter customers ID:  ")

                            if customer_filter != []:
                                key_filter = "Customer ID"
                                self.__customer_service.remove_customer(key_filter, customer_filter)
                            
                            else:
                                pass
                            
                            
                            print(indent,"b | Go back")
                            print(indent,"m | Go to Main menu")
                            print(indent,"q | Quit")
                            action = input(" Input letter: ").lower
                            if action == "m":
                                self.main_menu()
                            break
                                    

                    
                    elif action == "m":
                        # Go to Main menu
                        break

            
                        


                    
            
