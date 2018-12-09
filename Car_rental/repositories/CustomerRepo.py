import csv
from models.Customer import Customer

class CustomerRepo:

    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open("./data/customer.csv", "a+") as customers_file:
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

            csv_writer.writerow({"Customer ID": id_number, "Name": name, "Age": age, "Country": country, "Email": email,
            "Phone": phone, "Drivers License Number": dl_number, "Credit Card Number": cc_number})

    def get_customers(self):
        if self.__customer == []:
            with open("./data/customer.csv", "a+") as customers_file:
                cvs_reader = csv.DictReader(customers_file)

                    
