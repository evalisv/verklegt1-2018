import csv

class OrderRepo():
    def __init__(self):
        self.__order = []

    def add_order(self, order):
        with open('Car_rental/data/order.csv', 'a+') as order_file:
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
        with open('order.csv', 'r', newline='') as order_file:
            csv_reader = csv.reader(order_file)
            for row in csv_reader:
                if row[0] != number:
                    update_list.append(row)
                    
        #Overwrites file with list. New list has every order minus the one canceled.
        with open('order.csv', 'w', newline='') as order_file:
            csv_writer = csv.writer(order_file)
            for item in update_list:
                csv_writer.writerow(item)

    def change_order(self, number, old_value, new_value):
        
        #Same as cancel order, except the order is modified and then added to the update_list.
        update_list = []
        with open('order.csv', 'r', newline='') as order_file:
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
        
            
            
    
