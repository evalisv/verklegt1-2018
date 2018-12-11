from repositories.CarRepo import CarRepository
from repositories.CustomerRepo import CustomerRepo
from repositories.OrderRepo import OrderRepo

#price per day 
price_class_a = int(14900)
price_class_b = int(19900)
price_class_c = int(23900)
insurance_fee = int(1200)

date_format = "%m/%d/%Y"

class OrderService():
    def __init__(self):
        self.__order_repo = OrderRepo()

    # Calculate the price - Fallið ekki klárt þar sem það á eftir að sækja upplýsingar um flokkinn og tímalengd leigunnar
    def calculate_price(self, order):
        car_class = self.__order_repo.get_class(order)
        number_of_days = self.__order_repo.get_number_of_days(order)
        if car_class == "A":
            class_price = price_class_a
        elif car_class == "B":
            class_price = price_class_b
        elif car_class == "C":
            class_price = price_class_c
        price = (class_price * number_of_days) + (insurance_fee * number_of_days)
        return price

    def cancel_order(self, number):
        self.__order_repo.cancel_order(number)

    def change_order(self, number, old_value, new_value):
        self.__order_repo.change_order(number, old_value, new_value)

    def register_new_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def return_car(self, order):
        old_value = order.get_return_date()
        new_value = datetime.today()
        number = order.get_number()
        
        self.__order_repo.change_order(number, old_value, new_value)
            
        self.__car_repo.change_status(car)

        

    def rent_car(self, order):

    
