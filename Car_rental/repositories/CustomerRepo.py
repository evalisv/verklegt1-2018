import csv
from models.Customer import Customer

class CustomerRepo:

    def __init__(self):
        self.__customers = []

    def add_customer(self, customer):
        with open("data/customers.csv", "a+", encoding="utf-8") as customers_file:
            id_number = customer.get_id_number()
            first_name = customer.get_first_name()
            last_name = customer.get_last_name()
            age = customer.get_age()
            country = customer.get_country()
            email = customer.get_email()
            phone = customer.get_phone()
            dl_number = customer.get_dl_number()
            cc_number = customer.get_cc_number()

            fieldnames = ["Customer ID", "First Name", "Last Name", "Age", "Country", "Email", "Phone", "Drivers License Number", "Credit Card Number"]

            csv_writer = csv.DictWriter(customers_file, fieldnames=fieldnames, lineterminator="\n")

            csv_writer.writerow({"Customer ID": id_number, "First Name": first_name, "Last Name": last_name, "Age": age, "Country": country, "Email": email,
            "Phone": phone, "Drivers License Number": dl_number, "Credit Card Number": cc_number})

    def get_customers(self):
        with open ("data/customers.csv", "r", encoding = "utf-8") as customer_file:
            csv_list = []
            csv_reader = csv.reader(customer_file)   #Til þess að geta filterað út frá lyklum þarf að nota DictReader
            for line in csv_reader:
                if line not in csv_list:
                    csv_list.append(line)
                
            return csv_list