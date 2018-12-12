class Price:
    def __init__(self, category, price, insurance):
        self.__category = category
        self.__price = price
        self.__insurance = insurance

    def __str__(self):
        return "{},{},{}".format(
            self.__category, self.__price, self.__insurance)

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_insurance(self):
        return self.__insurance