import csv

class Customer:
    
    def __init__(self, id_number, name, age, country, email, phone, dl_number, cc_number):
        self.__id_number = id_number
        self.__name = name
        self.__age = age
        self.__country = country
        self.__email = email
        self.__phone = phone
        self.__dl_number = dl_number
        self.__cc_number = cc_number

    def __str__(self):
        return "{},{},{},{},{},{},{},{},".format(
            self.__id_number, self.__name, self.__age, self.__country, self.__email, self.__phone, self.__dl_number, self.__cc_number)
        
    def get_id_number(self):
        return self.__id_number

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_country(self):
        return self.__country

    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_dl_number(self):
        return self.__dl_number

    def get_cc_number(self):
        return self.__cc_number

class CustomerRepo:
    
    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open("Eva_testing_field/customer.csv", "a+") as customers_file:
            id_number = customer.get_id_number()
            name = customer.get_name()
            age = customer.get_age()
            country = customer.get_country()
            email = customer.get_email()
            phone = customer.get_phone()
            dl_number = customer.get_dl_number()
            cc_number = customer.get_cc_number()

            fieldnames = ["Customer ID", "Name", "Age", "Country", "Email", "Phone", "Drivers License Number", "Credit Card Number"]

            csv_writer = csv.DictWriter(customers_file, fieldnames=fieldnames, lineterminator="\n")

            csv_writer.writeheader()
            csv_writer.writerow({"Customer ID": id_number, "Name": name, "Age": age, "Country": country, "Email": email,
            "Phone": phone, "Drivers License Number": dl_number, "Credit Card Number": cc_number})



def main():
    id_number = input("ID: ")
    name = input("Name: ")
    age = input("Age: ")
    country = input("country: ")
    email = input("Email: ")
    phone = input("Phone: ")
    dl_number = input("DL_number: ")
    cc_number = input("CC_number: ")
    new_customer = Customer(id_number, name, age, country, email, phone, dl_number, cc_number)
    test = CustomerRepo()
    test.add_customer(new_customer)

main()