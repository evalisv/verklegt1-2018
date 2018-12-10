class Order:
    
    def __init__(self, number, customer_id, lp_number, pickup_date, return_date, price, insurance):
        self.__number = number
        self.__customer_id = customer_id
        self.__lp_number = lp_number
        self.__pickup_date = pickup_date
        self.__return_date = return_date
        self.__price = price
        self.__insurance = insurance

    def __str__(self):
        return "{},{},{},{},{},{},{},".format(
            self.__number, self.__customer_id, self.__lp_number, self.__pickup_date, self.__return_date, self.__price, self.__insurance)

    def get_order_number(self):
        return self.__number

    def get_customer_id(self):
        return self.__customer_id
    
    def get_lp_number(self):
        return self.__lp_number

    def get_pickup_date(self):
        return self.__pickup_date

    def get_return_date(self):
        return self.__return_date

    def get_price(self):
        return self.__price

    def get_insurance(self):
        return self.__insurance