from Services.CustomerService import CustomerService
from models.Customer import Customer

class CustomerUI:
    def __init__(self):
        self.__customer_service = CustomerService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("You can do the following:")
            print()
            print("1 | Register new customer")
            print("2 | List all customers")
            print("3 | Change customer information")
            print("4 | Remove customer from system")
            print("q | Quit program")
            print()

            action = input("Input number/letter: ").lower()

            if action == "1":
                id_number = input("ID number: ")
                name = input("Name: ")
                age = input("Age: ")
                country = input("Country: ")
                email = input("E-mail: ")
                phone = input("Phone number: ")
                dl_number = input("Drivers license number: ")
                cc_number = input("Credit Card number: ")
                new_customer = Customer(id_number, name, age, country, email, phone, dl_number, cc_number)
                self.__customer_service.add_customer(new_customer)