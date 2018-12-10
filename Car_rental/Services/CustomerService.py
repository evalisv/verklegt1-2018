<<<<<<< HEAD
<<<<<<< HEAD
from repositories.CustomerRepo import CustomerRepository

class CustomerService():
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_car(customer)
    
    def is_valid_customer(self, customer):
        #here should be some code to 
        #validate the customer
        return True

    def get_customers(self):
        return self.__customer_repo.get_customer()

    def get_customers_by_status(self, status):
        pass
=======
from Car_rental.models.Customer import Customer
=======
from repositories.CustomerRepo import CustomerRepo
>>>>>>> b64cd2ea8a29b23aca41aec1f64796794428b95e

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepo()

<<<<<<< HEAD
    def add_customer(self, )
>>>>>>> 3c0ef7acb2f0b5bdd9b9d84279a178ceb34f470e
=======
    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)
>>>>>>> b64cd2ea8a29b23aca41aec1f64796794428b95e
