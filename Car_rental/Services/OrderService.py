from repositories.CarRepo import CarRepository
from repositories.CustomerRepo import CustomerRepo
from repositories.OrderRepo import OrderRepo
from datetime import datetime

date_format = "%m/%d/%Y"

class OrderService():
    def __init__(self):
        self.__order_repo = OrderRepo()

    # Calculate the price - Fallið ekki klárt þar sem það á eftir að sækja upplýsingar um flokkinn og tímalengd leigunnar
    # def calculate_price(self, order):
    #     car_class = self.__order_repo.get_class(order)
    #     number_of_days = self.__order_repo.get_number_of_days(order)
    #     if car_class == "A":
    #         class_price = price_class_a
    #     elif car_class == "B":
    #         class_price = price_class_b
    #     elif car_class == "C":
    #         class_price = price_class_c
    #     price = (class_price * number_of_days) + (insurance_fee * number_of_days)
    #     return price

    def cancel_order(self, number):
        self.__order_repo.cancel_order(number)

    def change_order(self, number, old_value, new_value):
        self.__order_repo.change_order(number, old_value, new_value)

    def find_order(self, number):
        self.__order_repo.find_order(number)

    def register_new_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def return_car(self, order):
        old_value = order.get_return_date()
        new_value = datetime.today()
        number = order.get_number()
        
        self.__order_repo.change_order(number, old_value, new_value)
            
        self.__car_repo.change_status(car)

        

    def rent_car(self, order):
        pass
        

    def find_available_car(self, order):

        
        #Fall til að bera laus timabil við timabil sem er óskað í pöntun.
        def find_available_period(period_list, period_wanted_start, period_wanted_end):
            car_lp_list = []
            for period in period_list:         
                start_period = period[0]
                end_period = period[1]
                if period_wanted_start > start_period:
                    if period_wanted_end < end_period:
                        car_lp_list.append(car_lp)
            return car_lp_list


        #Breytir pick-up date og return date í datetime.
        period_wanted = [order.get_pickup_date(), order.get_return_date()]
        year, month, day = period_wanted[0].split(':')
        period_wanted_start = datetime(int(year), int(month), int(day))
        year, month, day = period_wanted[1].split(':')
        period_wanted_end = datetime(int(year), int(month), int(day))


        #Bý til lista af öllum bilum og bilum í pöntunum.
        car_list = self.__car_repo.get_cars_list()
        all_cars_list = []
        for cars in car_list:
            if cars['Category'] == order.get_category():
                car_list.append(cars['Licence Plate Number'])

        cars_in_orders = self.__order_repo.cars_in_orders(order)

        cars_in_orders_list = []
        for key, value in cars_in_orders:
            cars_in_orders_list.append(key)



        #Listi af lausum bilum sem er returnað.
        cars_available = []    


        #Kannar hvort til séu bilar sem eru ekki með pantanir skráðar.
        if len(cars_in_orders_list) != len(all_cars_list):
            for car in all_cars_list:
                if car not in cars_in_orders_list:
                    cars_available.append(car)
        #Ef enginn bill er alveg laus, leitar af bil sem er laus fyrir gefið timabil.
        else:
            for car_lp in cars_in_orders:    
                period_taken_list = cars_in_orders[car_lp]
                period_taken_list_datetime = []

                #Breytir leigutimabilum í pöntun í datetime.
                for item in period_taken_list:
                    year, month, day = (item[0]).split(':')
                    start_time = datetime(int(year), int(month), int(day))
                    year, month, day = (item[1]).split(':')
                    end_time = datetime(int(year), int(month), int(day))
                    period_taken = [start_time, end_time]
                    period_taken_list_datetime.append(period_taken)
        
                #Ef bill er bara skráður í eina pöntun.
                if len(period_taken_list) < 2:
                    
                    #Finn timabil þar sem bill er laus.
                    first_period = [datetime.now(), period_taken_list_datetime[0][0]]
                    last_period = [period_taken_list_datetime[0][1], (period_taken_list_datetime[0][1] + timedelta(days=365))]        
                    period_available = [first_period, last_period]
                    car_list = find_available_period(period_available, period_wanted_start, period_wanted_end)
                    cars_available.append(car_list)
        
                #Ef bill er skraður í fleiri en einni pöntun.
                else:
        
                    #Fæ lengd 
                    list_length = len(period_taken_list_datetime)
                    
                    #Fyrsta lausa timabil er frá deginum í dag til fyrsta pickup date.
                    first_period = [datetime.now(), period_taken_list_datetime[0][0]]
                    #Seinasta lausa timabil er frá seinasta return date + ár fram í timann.
                    last_period = [period_taken_list_datetime[len(period_taken_list_datetime) - 1][1], (period_taken_list_datetime[len(period_taken_list_datetime) - 1][1] + timedelta(days=365))]

                    period_available = [first_period]
    
                    index = 0
                    #Finn timabil þar sem bill er laus.
                    while index <= (len(period_taken_list_datetime) - 2):
                        available_period = [(period_taken_list_datetime)[index][1], (period_taken_list_datetime)[(index + 1)][0]]
                        period_available.append(available_period)
                        index += 1

                    period_available.append(last_period)

                    car_list = find_available_period(period_available, period_wanted_start, period_wanted_end)

                    cars_available.append(car_list)

        return cars_available

    
