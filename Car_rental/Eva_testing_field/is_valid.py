import csv
class Customer:
    def __init__(self, id_number, first_name, last_name, age, country, email, phone, dl_number, cc_number):
        self.__id_number = id_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__country = country
        self.__email = email
        self.__phone = phone
        self.__dl_number = dl_number
        self.__cc_number = cc_number

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(
            self.__id_number, self.__first_name, self.__last_name ,self.__age, self.__country, self.__email, self.__phone, self.__dl_number, self.__cc_number)
        
    def get_id_number(self):
        return self.__id_number

    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
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
        self.__customers = []

    def add_customer(self, customer):
        with open("Eva_testing_field/customer.csv", "a+", encoding="utf-8") as customers_file:
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
        with open ("Eva_testing_field/customer.csv", "r", encoding = "utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            if self.__customers == []:
                for line in csv_reader:
                    self.__customers.append(line)

        return self.__customers

    
    def remove_customer(self, new_value):
        self.__new_value = new_value
        with open ("Eva_testing_field/customer.csv", "w", encoding = "utf-8") as changed_csv:
            fieldnames = ["Customer ID", "First Name", "Last Name", "Age", "Country", "Email", "Phone", "Drivers License Number", "Credit Card Number"]
            csv_writer = csv.DictWriter(changed_csv, fieldnames = fieldnames, lineterminator = "\n")
            csv_writer.writeheader()
            for line in new_value:
                csv_writer.writerow(line)
        pass

    
    def change_customer(self, new_value):
        self.__new_value = new_value
        with open ("Eva_testing_field/customer.csv", "w", encoding = "utf-8") as changed_csv:
            fieldnames = ["Customer ID", "First Name", "Last Name", "Age", "Country", "Email", "Phone", "Drivers License Number", "Credit Card Number"]
            csv_writer = csv.DictWriter(changed_csv, fieldnames = fieldnames, lineterminator = "\n")
            csv_writer.writeheader()
            for line in new_value:
                csv_writer.writerow(line)
    
    def get_customer_id(self):
        return Customer.get_id_number(self)
        

class CustomerService():
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def add_customer(self, new_customer):
        self.__new_customer = new_customer
        #new_customer_list = self.__new_customer.split(",")
        validation =self.is_valid_customer(new_customer)
        if validation == True:
            print()
            action = ""
            print("Confirm registration?")
            action = input("Y/N: ").lower()
            if action == "y":
                
                self.__customer_repo.add_customer(new_customer)
                print()
                print("Customer successfully registered!")
            else:
                print()
                print("Customer registration canceled.")
                pass


    def is_valid_customer(self, new_customer):
        print("In is_valid_customer")
        self.__new_customer = new_customer
        new_customer_str = str(new_customer)
        customer_id, first_name, last_name, age,country, email, phone, dl_number, cc_number = new_customer_str.split(",")
        while True:
            try:
                if len(customer_id) > 10:
                    raise ValueError
            except ValueError:
                print("Customer ID given was too long. Please try again.")
                
            

    def get_customers(self):
        print()
        print("List of all customers")
        print()
        print(" ","{:<20} {:<40} {:<40} {:<20} {:<20}".format("Customer ID", "Full name", "Email", "Phone", "Country"))
        print("-"*140)
        for line in self.__customer_repo.get_customer_list():
            full_name = "{} {}".format(line["First Name"], line["Last Name"])
            print(" ","{:<20} {:40} {:40} {:<20} {:<20}".format(line["Customer ID"], full_name, line["Email"], line["Phone"], line["Country"]))
        return

    def change_customer_info(self, key, key_filter,customer_filter):
        self.__customer_filter = customer_filter
        self.__key = key
        self.__key_filter = key_filter
        match_value = 1
        customer_list = self.__customer_repo.get_customer_list()
        for line in customer_list:
            
            if line[key_filter] == customer_filter:
                print()
                print(" Information to be changed:", line[key])
                new_value = input(" Correct information: ")
                old_info = line[key]
                line[key] = new_value
                match_value += 1
                
        if match_value == 1:
            # Notify that something wasn't found
            print()
            print(" No customer found")

        if match_value != 1:
            self.__customer_repo.change_customer(customer_list)
            print()
            print(" Success! Customer information has been changed changed from", old_info, "to", new_value)

    def find_customer(self, customer_id):
        self.__customer_id = customer_id
        match_value = 1
        customer_list = self.__customer_repo.get_customer_list()
        for line in customer_list:
            
            if line["Customer ID"] == customer_id:
                full_name = "{} {}".format(line["First Name"], line["Last Name"])
                
                match_value += 1
                break
                
        if match_value == 1:
            # Notify that something wasn't found
            print()
            print(" No customer found")
        
        if match_value != 1:
            print()
            print("You found this customer:")
            print()
            print(" ","{:<20} {:<40} {:<40} {:<20} {:<20}".format("Customer ID", "Full name", "Email", "Phone", "Country"))
            print("-"*140)
            print(" ","{:<20} {:40} {:40} {:<20} {:<20}".format(line["Customer ID"], full_name, line["Email"], line["Phone"], line["Country"]))

        
 
    def remove_customer(self, key_filter, customer_filter):
        self.__customer_filter = customer_filter
        self.__key_filter = key_filter
        match_value = 1
        customer_list = self.__customer_repo.get_customer_list()
        for line in customer_list:
            
            if line[key_filter] == customer_filter:
                print(" Customer to be removed:", line["First Name"], line["Last Name"])
                match_value += 1
                print(" Confirm removal?")
                action = input( "Y/N: ").lower()
                if action == "y":
                    customer_list.remove(line)
                if action == "n":
                    print(" Customer removal canceled")
                    print(" Do you want to try again?")
                    try_again = input("Y/N")
                    if try_again == "y":
                        return False
                    else:
                        return True
        if match_value == 1:
            # Notify that something wasn't found
            print(" No customer with given ID found.Do you want to try again?")
            try_again = input("Y/N")
            if try_again == "y":
                return False
            else:
                return True
        if match_value != 1 and action =="y":
            self.__customer_repo.remove_customer(customer_list)
            print(" Success! Customer has been removed from the system")
            return True
def main():

    id_number = input("ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = input("Age: ")
    country = input("country: ")
    email = input("Email: ")
    phone = input("Phone: ")
    dl_number = input("DL_number: ")
    cc_number = input("CC_number: ")
    new_customer = Customer(id_number, first_name, last_name, age, country, email, phone, dl_number, cc_number)
    service = CustomerService()
    service.add_customer(new_customer)

main()