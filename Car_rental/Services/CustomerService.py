from Car_rental.models.Customer import Customer

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def add_customer(self, )