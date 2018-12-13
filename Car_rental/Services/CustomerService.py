from repositories.CustomerRepo import CustomerRepo

class CustomerService():
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def add_customer(self, new_customer):
        self.__new_customer = new_customer
        #new_customer_list = self.__new_customer.split(",")
        if self.is_valid_customer(new_customer):
            print()
            action = ""
            print("Confirm registration?")
            action = input("Y/N: ").lower()
            if action == "y":
                
                self.__customer_repo.add_customer(new_customer)
                print("Customer successfully registered!")
            else:
                print("Customer registration canceled.")
                pass
    def is_valid_customer(self, customer):
        #here should be some code to 
        #validate the customer
        return True

    def get_customers(self):
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
                print(" Information to be changed:", line[key])
                new_value = input(" Correct information: ")
                old_info = line[key]
                line[key] = new_value
                match_value += 1
                
        if match_value == 1:
            # Notify that something wasn't found
            print(" No customer found")

        if match_value != 1:
            self.__customer_repo.change_customer(customer_list)
            print(" Success! Customer information has been changed changed from", old_info, "to", new_value)

        
 
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
                else:
                    print(" Customer removal canceled")
                    pass
        if match_value == 1:
            # Notify that something wasn't found
            print(" No customer with given ID found.")

        if match_value != 1 and action =="y":
                self.__customer_repo.remove_customer(customer_list)
                print(" Success! Customer has been removed from the system")

        return