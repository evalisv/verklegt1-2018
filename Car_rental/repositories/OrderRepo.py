import csv
from models.Order import Order
from datetime import datetime

date_format = "%d.%m.%y"

class OrderRepo():
    def __init__(self):
        self.__orders_list = []

    def add_order(self, order):
        with open('Data/orders.csv', 'a+', encoding = "utf-8") as order_file:
            number = order.get_order_number()
            customer_id = order.get_customer_id()
            category = order.get_category()
            lp_number = order.get_lp_number()
            pickup_date = order.get_pickup_date()
            return_date = order.get_return_date()
            price = order.get_price()
            insurance = order.get_insurance()
            actual_day_of_return = order.get_actual_return_date()

            fieldnames = ["Number", "Customer", "License Plate Number", "Category",
             "Pick-up Date", "Return Date", "Price", "Insurance", "Actual day of return"]

            csv_writer = csv.DictWriter(order_file, fieldnames=fieldnames, lineterminator = "\n")
            #Spurning með writeheader. Virðist adda header með hverri nýrri línu.
            
            csv_writer.writerow({'Number': number, 'Customer': customer_id, 'License Plate Number': lp_number,
                             'Category': category, 'Pick-up Date': pickup_date,
                            'Return Date': return_date, 'Price': price, 'Insurance': insurance, "Actual day of return" : actual_day_of_return})

    def find_order(self, number):
        with open('Data/orders.csv', 'r', encoding = "utf-8") as order_file:
            csv_reader = csv.reader(order_file)
            for row in csv_reader:
                if row[0] == number:
                    return row

    def get_order_list(self):
        with open ("Data/orders.csv", "r", encoding = "utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                if line not in self.__orders_list:
                    self.__orders_list.append(line)
        return self.__orders_list
    
    def cancel_order(self, number):
        #Puts every orders into a list, except the one you want to cancel
        update_list = []
        with open('Data/orders.csv', 'r', encoding = "utf-8") as order_file:
            csv_reader = csv.reader(order_file)
            for row in csv_reader:
                if row["Number"] != number:
                    update_list.append(row)
                 
        #Overwrites file with list. New list has every order minus the one canceled.
        with open('Data/orders.csv', 'w', encoding = "utf-8", lineterminator = "\n") as order_file:
            csv_writer = csv.writer(order_file)
            for item in update_list:
                csv_writer.writerow(item)

    def change_order(self, order, index, actual_return_date):
        
        
        #Same as cancel order, except the order is modified and then added to the update_list.
        update_list = []
        with open('Data/orders.csv', 'r', encoding = "utf-8") as order_file:
            csv_reader = csv.reader(order_file)
            for row in csv_reader:
                if row == []:
                    pass
                else:
                    if row[0] == order:
                        index = int(index)
                        row[index] = actual_return_date
                        update_list.append(row)
                    else:
                        update_list.append(row)

       

        #Overwrites file with list. New file includes changed order.
        with open('Data/orders.csv', 'w', encoding = "utf-8", newline='') as order_file:
            fieldnames = ['License Plate Number', 'Category', 'Model', 'Brand', 'Colour', 'Year', 'Kilometers', 'Status']
            csv_writer = csv.writer(order_file)
            
            for line in update_list:        
                csv_writer.writerow(line)

    #Fer í gegnum pantanir og setur bilana í dictionary.
    #dictionary key = bílnúmer, key = leigutimabil pantanna.
    def cars_in_orders(self, category):
        period_taken_dict = {}
        with open('Data/orders.csv', 'r', encoding = "utf-8") as order_file:
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
    
    def list_of_orders(self, category):
        new_list_of_orders = []
        with open('Data/orders.csv', 'r', encoding = "utf-8") as order_file:
            csv_reader = csv.DictReader(order_file)
            for order in csv_reader:
                order_info = [order["License Plate Number"], order["Pick-up Date"], order["Return Date"]]
                if order["Category"] == category:
                    new_list_of_orders.append(order_info)
        return new_list_of_orders
            


    # def get_number_of_days(self, order):
    #     start = datetime.strptime(self.order.get_pickup_date(order), date_format)
    #     start = datetime.strptime(self.order.get_pickup_date(order), date_format)
    #     end = datetime.strptime(self.order.get_return_date(order), date_format)
    #     number_of_days = end - start
    #     return number_of_days

    
    def find_next_order_number(self):
        number_list = []
        with open('Data/orders.csv', 'r', encoding = "utf-8") as order_file:
            
            csv_reader = csv.reader(order_file)
            for row in csv_reader:
                if row == []:
                    pass
                else:                 
                    number = row[0]
                    if number.isdigit():
                        number = int(number)
                        number_list.append(number)
            try:
                highest_number = max(number_list)
            except:
                highest_number = 100
            
            next_order_number = highest_number + 1
            
        return next_order_number


        
            # Á eftir að bæta við virkni í skráningu á orders. Í framhaldi þarf svo að laga þessi föll

    # def get_class(self, order):
    #     return self.order.get_class(order)
    
    # def get_number_of_days(self, order):
    #     start = datetime.strptime(self.order.get_pickup_date(order), date_format)
    #     end = datetime.strptime(self.order.get_return_date(order), date_format)
    #     number_of_days = end - start
    #     return number_of_days
