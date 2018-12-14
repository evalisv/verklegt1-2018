from repositories.CarRepo import CarRepo
from repositories.CustomerRepo import CustomerRepo
from repositories.OrderRepo import OrderRepo
from Services.PriceService import PriceService
from Services.CarService import CarService
from Services.CustomerService import CustomerService
from datetime import datetime
from datetime import timedelta
from models.Customer import Customer
from models.Car import Car
from models.Order import Order
from models.Price import Price

class OrderService():
    def __init__(self):
        self.__order_repo = OrderRepo()
        self.__customer_repo = CustomerRepo()
        self.__car_repo = CarRepo()
        self.__price_service = PriceService()

    def add_order(self, order):
        self.__order_repo.add_order(order)
    


    def cancel_order(self):
        number = input('Enter order number: ')
        self.__order_repo.cancel_order(number)

    def change_order(self):
        number = input('Enter number')
        index = input('Enter index:')
        new_value = input('Enter new value')
        self.__order_repo.change_order(number, index, new_value)

    def find_order(self):
        number = input('Enter order number: ')
        order = self.__order_repo.find_order(number)
        print(order)

    def register_new_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def return_car(self, order):
        old_value = order.get_return_date()
        new_value = datetime.today()
        number = order.get_number()
        
        self.__order_repo.change_order(number, old_value, new_value)
            
        self.__car_repo.change_status(car)

    def find_next_order_number(self):
        self.__order_repo.find_next_order_number()

        

    def rent_car(self):
        category = input('Enter Category: ')
        pick_up_date = input('Enter pick-up date(Y:M:D):')
        number_of_days = input('Enter number of days:')
        insurance = input('Insurance? (Yes/No)')
        customer_id = input('Enter customer id: ')
        #number = input('Enter order number:')

        

        order = Order()
        order.category = category
        order.pickup_date = pick_up_date

        order.customer_id = customer_id
        order.insurance = insurance
        number = self.find_next_order_number()
        order.number = number
        return_date = self.calculate_return_date(pick_up_date, number_of_days)
        order.return_date = return_date
        nr_of_days = int(number_of_days)
        available_car_lp = self.find_available_car(category, pick_up_date, return_date)
        order.lp_number = available_car_lp
                                
        price = self.__price_service.calculate_price_for_order(category, nr_of_days)

        order.price = price
        self.add_order(order)
        pass

    def calculate_return_date(self, pickup_date, nr_days):
        year, month, day = pickup_date.split(':')
        pickup_date_datetime = datetime(int(year), int(month), int(day))
        days = int(nr_days)
        return_date = (pickup_date_datetime + timedelta(days=days))
        return_date = return_date.strftime('%Y/%m/%d')
        year, month, day = return_date.split('/')
        if month[0] == '0':
            month = month[1]
        if day[0] == '0':
            day = day[1]
        return_date_format = year + ':' + month + ':' + day
        
        return return_date_format
        
        

    def find_available_car(self, category, pick_up_date, return_date):

        
        #Fall til að bera laus timabil við timabil sem er óskað í pöntun.
        def find_available_period(period_list, period_wanted_start, period_wanted_end):
            car_lp_list = []
            for period in period_list:         
                start_period = period[0]
                end_period = period[1]
                if period_wanted_start > start_period:
                    if period_wanted_end < end_period:
                        car_lp_list.append(car_lp)
            return car_lp_list[0]


        #Breytir pick-up date og return date í datetime.
        period_wanted = [pick_up_date, return_date]
        year, month, day = period_wanted[0].split(':')
        period_wanted_start = datetime(int(year), int(month), int(day))
        year, month, day = period_wanted[1].split(':')
        period_wanted_end = datetime(int(year), int(month), int(day))


        #Bý til lista af öllum bilum og bilum í pöntunum.
        car_list = self.__car_repo.get_cars_list()
        all_cars_list = []
        for cars in car_list:
            if cars['Category'] == category:
                all_cars_list.append(cars['License Plate Number'])

        cars_in_orders = self.__order_repo.cars_in_orders(category)

        cars_in_orders_list = list(cars_in_orders.keys())
        



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

        return cars_available[0]

    
