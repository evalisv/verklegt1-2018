from repositories.CustomerRepo import CustomerRepo

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)