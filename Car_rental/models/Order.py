class Order:
    
    def __init__(self, number = '', customer_id = '', lp_number = '', category = '', pickup_date = '', return_date = '', price = '', insurance = ''):
        self.number = number
        self.customer_id = customer_id
        self.lp_number = lp_number
        self.category = category
        self.pickup_date = pickup_date
        self.return_date = return_date
        self.price = price
        self.insurance = insurance

    def __str__(self):
        return "{},{},{},{},{},{},{},".format(
            self.number, self.customer_id, self.lp_number, self.pickup_date, self.return_date, self.price, self.insurance)

    def get_order_number(self):
        return self.number

    def get_customer_id(self):
        return self.customer_id
    
    def get_lp_number(self):
        return self.lp_number

    def get_category(self):
        return self.category

    def get_pickup_date(self):
        return self.pickup_date

    def get_return_date(self):
        return self.return_date

    def get_price(self):
        return self.price

    def get_insurance(self):
        return self.insurance
