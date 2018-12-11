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

    def get_customer_list(self):
        customer_list = []
        with open ("Data/customers.csv", "r", encoding = "utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)   #Til þess að geta filterað út frá lyklum þarf að nota DictReader
            if customer_list == []:
                for line in csv_reader:
                    customer_list.append(line)

        return customer_list

    
    def remove_customer(self):
        pass
    
    
    def change_customer(self):
        # update_list = []
        # with open("data/customers", "r", encoding = "utf-8", lineterminator = "\n") as customer_file:
        #     csv_reader = csv.DictReader(customer_file)
        #     for line in csv_reader:
        #         if line["Customer ID"] == id_number_filter:
                    
        #             change_row = row
        #             index = row.index(old_value)
        #             change_row[index] = new_value
        #             update_list.append(change_row)
        #         else:
        #             update_list.append(row)
        pass

        #Overwrites file with list. New file includes changed order.
        with open('order.csv', 'w', newline='') as order_file:
            csv_writer = csv.writer(order_file)
            for order in update_list:
                csv_writer.writerow(order)
                