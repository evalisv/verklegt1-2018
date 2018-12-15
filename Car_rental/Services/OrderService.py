from repositories.CarRepo import CarRepo
from repositories.CustomerRepo import CustomerRepo
from repositories.OrderRepo import OrderRepo
from Services.PriceService import PriceService
from Services.CarService import CarService
from Services.CustomerService import CustomerService
from datetime import datetime
from datetime import timedelta
from datetime import date
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
    
    def get_orders(self):
        print()
        print(45*"-","List of all orders",45*"-")
        print()
        print(" ","{:<20} {:<20} {:<20} {:<20}".format("Customer", "License Plate Number", "Pick-up Date", "Return Date"))
        print("-"*120)
        for line in self.__order_repo.get_list_of_orders():
            print(" ","{:<20} {:<20} {:<20} {:<20}".format(line["Customer"], line["License Plate Number"], line["Pick-up Date"], line["Return Date"]))
        return

    def cancel_order(self, order_filter):
        
        self.__order_filter = order_filter
        match_value = 1
        order_list = self.__order_repo.get_list_of_orders()
        for line in order_list:
            
            if line["Number"] == order_filter:
                print(" Order to be removed:", line["Number"])
                match_value += 1
                print(" Confirm removal?")
                action = input( "Y/N: ").lower()
                if action == "y":
                    order_list.remove(line)
                if action == "n":
                    print(" Order removal canceled")
                    print(" Do you want to try again?")
                    try_again = input("Y/N: ").lower()
                    if try_again == "y":
                        return False
                    else:
                        return True
        if match_value == 1:
            # Notify that something wasn't found
            print(" No order with given number found. Do you want to try again?")
            try_again = input("Y/N: ")
            if try_again == "y":
                return False
            else:
                return True
        if match_value != 1 and action =="y":
            self.__order_repo.cancel_order(order_list)
            print(" Success! Order has been removed from the system")
            return True

    def change_order(self, key_filter, order_filter, key):
        self.__key_filter = key_filter
        self.__key = key
        self.__order_filter = order_filter
        match_value = 1
        order_list = self.__order_repo.get_list_of_orders()
        for line in order_list:
            
            if line[key_filter] == order_filter:
                print()
                print(" Information to be changed:", line[key])
                new_value = input(" Correct information: ")
                old_info = line[key]
                line[key] = new_value
                match_value += 1
                
        if match_value == 1:
            # Notify that something wasn't found
            print()
            print(" No order found")

        if match_value != 1:
            self.__order_repo.change_order(order_list)
            print()
            print(" Success! Order information has been changed from", old_info, "to", new_value)

    def find_order(self):
        number = input('Enter order number: ')
        order = self.__order_repo.find_order(number)
        print(order)

    def register_new_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def return_car(self, order_number):
        
        new_value = datetime.today()
        index = 8
        
        
        self.__order_repo.return_car(order_number, index, new_value)
    # virkar
    def find_next_order_number(self):
        number = self.__order_repo.find_next_order_number()
        return number


    def rent_car(self, new_order):
        

        number, customer_id, lp_number, category, pickup_date, return_date, price, insurance, actual_return_date = str(new_order).split(",")
        #number = '', customer_id = '', lp_number = '', category = '', pickup_date = '', return_date = '', price = '', insurance = ''
        # self.__order_repo.__category = category
        # self.__order_repo.__pickup_date = pickup_date
        # self.__order_repo.__return_date = return_date
        # self.__order_repo.__customer_id = customer_id
        # self.__order_repo.__insurance = insurance
        # self.__order_repo.number = self.find_next_order_number()
        days = self.number_of_days(pickup_date, return_date)
        number = self.find_next_order_number()
        available_car_lp = self.find_available_car(category, pickup_date, return_date)
        lp_number = available_car_lp
        price = self.__price_service.calculate_price_for_order(category, days, insurance)
        order = Order(number, customer_id, lp_number, category, pickup_date, return_date, price, insurance, actual_return_date)
        self.__order_repo.price = price
        self.__order_repo.add_order(order)





    def number_of_days(self, pickup_date, return_date):

        day, month, year = pickup_date.split('.')
        pickup_date_datetime = datetime(int(year), int(month),int(day))
        day, month, year = return_date.split('.')
        return_date_datetime = datetime(int(year), int(month),int(day))

        number_of_days = (return_date_datetime - pickup_date_datetime)
        number_of_days = int(number_of_days.days)
        return number_of_days
        
        

    def find_available_car(self, category, pickup_date, return_date):
       
        day, month, year = pickup_date.split('.')
        pickup_date_datetime = datetime(int(year), int(month),int(day))
        day, month, year = return_date.split('.')
        return_date_datetime = datetime(int(year), int(month),int(day))
        
        available_car_list = []
        car_list = self.__car_repo.get_cars_list()
        order_list = self.__order_repo.get_list_of_orders()

        for car in car_list:
            for order in order_list:
                if car in order_list and ((car["Return Date"] < order["Pick-up Date"]) and car["Pick-up Date"] > order["Return Date"]) and car not in available_car_list:
                    available_car_list.append(car)


        # Merg13:00
        #  day, month, year = pickup_date.split('.')
        # pickup_date_datetime = datetime(int(year), int(month),int(day))
        # day, month, year = return_date.split('.')
        # return_date_datetime = datetime(int(year), int(month),int(day))

        # car.get_category()


        #Bý til lista af öllum bilum í réttu category og bilum í pöntunum.
        car_list = self.__car_repo.get_cars_list()
        cars_in_category = [car for car in car_list if car["Category"] == category]
        lp_in_category = [str(car["License Plate Number"]) for car in car_list if car["Category"] == category]
        


            
        cars_in_orders = self.__order_repo.cars_in_orders(category)
        list_of_orders = self.__order_repo.list_of_orders(category)
        cars_taken = []
        cars_available = []
        
        for order in list_of_orders:
            
            lp_number = str(order[0])
            
            order_pickup = order[1]
            order_return = order[2]
            day, month, year = order_pickup.split('.')
            order_pickup = datetime(int(year), int(month),int(day))
            day, month, year = order_return.split('.')
            order_return = datetime(int(year), int(month),int(day))
            if order_pickup < return_date_datetime and order_return > pickup_date_datetime:
                cars_taken.append(lp_number)
            
        for car in lp_in_category:
            if car not in cars_taken:
                cars_available.append(car)
        
        # cars_in_orders_list = list(cars_in_orders.keys())
        # print(cars_in_orders_list)
        # if len(cars_in_orders) == 0:
        # min_used_car = min(cars_available, key=lambda Car: int(car.get_km()))
        # print(min_used_car)
        # print(type(min_used_car))
        # return getattr(min_used_car,)
        try:
            return cars_available[0]
        except:
            print("No car available")

    
   
    




###################################################################################
######################### Bannsvæði hér að neðan! #################################
################################# grín?? ##########################################
############################ Fúlasta alvara #######################################


        # #Breytir pick-up date og return date í datetime.
        # period_wanted = [pickup_date, return_date]
        # year, month, day = period_wanted[0].split('.')
        # period_wanted_start = datetime( int(day), int(month), int(year))
        # year, month, day = period_wanted[1].split('.')
        # period_wanted_end = datetime( int(day), int(month), int(year))



        #Listi af lausum bilum sem er returnað.
        # cars_available = []    

    # def find_available_period(period_list, period_wanted_start, period_wanted_end):
    #     car_lp_list = []
    #     for period in period_list:         
    #         start_period = period[0]
    #         end_period = period[1]
    #         if period_wanted_start > start_period:
    #             if period_wanted_end < end_period:
    #                 car_lp_list.append(car_lp)
    #     try:
    #         return car_lp_list[0]
    #     except:
    #             print("No car available")


        #Kannar hvort til séu bilar sem eru ekki með pantanir skráðar.
        # if len(cars_in_orders_list) != len():
        #     for car in all_cars_list:
        #         if car not in cars_in_orders_list:
        #             cars_available.append(car)
        # Ef enginn bill er alveg laus, leitar af bil sem er laus fyrir gefið timabil.
        # elif:
        #     for car_lp in cars_in_orders:    
        #         print(car_lp)
        #         period_taken_list = cars_in_orders[car_lp]
        #         period_taken_list_datetime = []

                #Breytir leigutimabilum í pöntun í datetime.
                # for item in period_taken_list:
                #     year, month, day = (item[0]).split(':')
                #     start_time = datetime(int(year), int(month), int(day))
                #     year, month, day = (item[1]).split(':')
                #     end_time = datetime(int(year), int(month), int(day))
                #     period_taken = [start_time, end_time]
                #     period_taken_list_datetime.append(period_taken)
        
                #Ef bill er bara skráður í eina pöntun.
                # if len(period_taken_list) < 2:
                    
                    #Finn timabil þar sem bill er laus.
                # first_period = [datetime.now(), period_taken_list_datetime[0][0]]
                # last_period = [period_taken_list_datetime[0][1], (period_taken_list_datetime[0][1] + timedelta(days=365))]        
                # period_available = [first_period, last_period]
                # print(period_available)
                # car_list = find_available_period(period_available, period_wanted_start, period_wanted_end)
                # print(car_list)
                # cars_available.append(car_list)
                # print(cars_available)
        
                #Ef bill er skraður í fleiri en einni pöntun.
        # else:

        #     #Fæ lengd 
        #     list_length = len(period_taken_list_datetime)
            
        #     #Fyrsta lausa timabil er frá deginum í dag til fyrsta pickup date.
        #     first_period = [datetime.now(), period_taken_list_datetime[0][0]]
        #     #Seinasta lausa timabil er frá seinasta return date + ár fram í timann.
        #     last_period = [period_taken_list_datetime[len(period_taken_list_datetime) - 1][1], (period_taken_list_datetime[len(period_taken_list_datetime) - 1][1] + timedelta(days=365))]

        #     period_available = [first_period]

        #     index = 0
        #     #Finn timabil þar sem bill er laus.
        #     while index <= (len(period_taken_list_datetime) - 2):
        #         available_period = [(period_taken_list_datetime)[index][1], (period_taken_list_datetime)[(index + 1)][0]]
        #         period_available.append(available_period)
        #         index += 1

        #     period_available.append(last_period)

        #     car_list = find_available_period(period_available, period_wanted_start, period_wanted_end)

        #     cars_available.append(car_list)
        #     print(cars_available)

        # try:
        #     return cars_available[0]
        # except:
        #     print("No available car")
        #     return None
    
