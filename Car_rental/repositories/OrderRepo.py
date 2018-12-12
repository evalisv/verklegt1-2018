import csv
from models.Order import Order
from datetime import datetime

date_format = "%m/%d/%Y"

class OrderRepo():
    def __init__(self):
        self.__order = []

    def add_order(self, order):
        with open('Car_rental/data/order.csv', 'a+', encoding = "utf-8") as order_file:
            number = order.get_order_number()
            customer_id = order.get_customer_id()
            lp_number = order.get_lp_number()
            pickup_date = order.get_pickup_date()
            return_date = order.get_return_date()
            price = order.get_price()
            insurance = order.get_insurance()

            fieldnames = ['Number', 'Customer ID', 'License Plate Number', 'Pick-up Date', 'Return Date', 'Price', 'Insurance']

            csv_writer = csv.DictWriter(order_file, fieldnames=fieldnames, lineterminator="\n")
            #Spurning með writeheader. Virðist adda header með hverri nýrri línu.
            csv_writer.writeheader()
            csv_writer.writerow({'Number': number, 'Customer': customer_id, 'License Plate Number': lp_number, 'Pick-up Date': pickup_date,
                            'Return Date': return_date, 'Price': price, 'Insurance': insurance})

    def cancel_order(self, number):

        #Puts every orders into a list, except the one you want to cancel
        update_list = []
        with open('order.csv', 'r', encoding = "utf-8", lineterminator = "\n") as order_file:
            csv_reader = csv.reader(order_file)
            for row in csv_reader:
                if row[0] != number:
                    update_list.append(row)
                    
        #Overwrites file with list. New list has every order minus the one canceled.
        with open('order.csv', 'w', encoding = "utf-8", lineterminator = "\n") as order_file:
            csv_writer = csv.writer(order_file)
            for item in update_list:
                csv_writer.writerow(item)

    def change_order(self, number, old_value, new_value):
        
        #Same as cancel order, except the order is modified and then added to the update_list.
        update_list = []
        with open('order.csv', 'r', encoding = "utf-8", lineterminator = "\n") as order_file:
            csv_reader = csv.reader(order_file)
            for row in csv_reader:
                if row[0] == number:
                    change_row = row
                    index = row.index(old_value)
                    change_row[index] = new_value
                    update_list.append(change_row)
                else:
                    update_list.append(row)

        #Overwrites file with list. New file includes changed order.
        with open('order.csv', 'w', newline='') as order_file:
            csv_writer = csv.writer(order_file)
            for order in update_list:
                csv_writer.writerow(order)

    #Fer í gegnum pantanir og setur bilana í dictionary.
    #dictionary key = bílnúmer, key = leigutimabil pantanna.
    def cars_in_orders(self, order):
        period_taken_dict = {}
        with open('orders.csv', 'r', encoding = "utf-8") as order_file:
            csv_reader = csv.DictReader(order_file)
            for order in csv_reader:
                period_taken = [order['Pick-up Date'], order['Return Date']]
                car_lp = order['License Plate Number']
                if order['Category'] == category:
                    if car_lp in period_taken_dict:
                        period_taken_dict[car_lp].append(period_taken)
                    else:
                        period_taken_dict[car_lp] = [period_taken]
        return period_taken_dict
        

            # Á eftir að bæta við virkni í skráningu á orders. Í framhaldi þarf svo að laga þessi föll

    # def get_class(self, order):
    #     return self.order.get_class(order)
    
    # def get_number_of_days(self, order):
    #     start = datetime.strptime(self.order.get_pickup_date(order), date_format)
    #     end = datetime.strptime(self.order.get_return_date(order), date_format)
    #     number_of_days = end - start
    #     return number_of_days
