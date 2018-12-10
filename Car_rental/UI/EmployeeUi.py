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
                action = ""
                while(action != "q"):    
                    print("You can do the following:")
                    print()
                    print("1 | See Available cars")
                    print("2 | See Unavailable cars")
                    print("3 | List of all cars")
                    print("4 | See Details of a car")
                    print("q | Quit")
                    print()
                    
                    action = input("Input number/letter: ").lower()

            if action == "2":
                # Goes to Orders menu
                pass

            if action == "3":
                # Goes to Customers menu
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
                        break
                        


                    
            
