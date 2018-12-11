from repositories.CustomerRepo import CustomerRepo

class CustomerService():
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def is_valid_customer(self, customer):
        #here should be some code to 
        #validate the customer
        return True

    def get_customers(self):
        print("{:<15} {:<20} {:<30} {:<15} {:<15}".format("Customer ID", "Full name", "Email", "Phone", "Country"))
        print("-"*95)
        for line in self.__customer_repo.get_customer_list():
            full_name = "{} {}".format(line["First Name"], line["Last Name"])
            print("{:<15} {:<20} {:<30} {:<15} {:<15}".format(line["Customer ID"], full_name, line["Email"], line["Phone"], line["Country"]))
        return

    def get_customers_by_status(self, status):
        pass

    def remove_customer(self):
        pass
