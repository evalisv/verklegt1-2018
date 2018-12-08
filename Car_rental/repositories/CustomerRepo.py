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

            fieldnames = ["id_number", "name", "age", "country", "email", "phone", "dl_number", "cc_number"]

            csv_writer = csv.DictWriter(customers_file, fieldnames=fieldnames, lineterminator="\n")

            csv_writer.writeheader()
            csv_writer.writerow({"id_number": id_number, "name": name, "age": age, "country": country, "email": email,
            "dl_number": dl_number, "cc_number": cc_number})

