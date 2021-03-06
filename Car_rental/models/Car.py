class Car:
    def __init__(self, lp_number, category, brand, model,  colour, year, km, status):
        self.__category = category
        self.__lp_number = lp_number
        self.__brand = brand
        self.__model =  model
        self.__year = year
        self.__km = km
        self.__colour = colour
        self.__status = status

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(
            self.__lp_number, self.__category, self.__brand, self.__model, self.__colour, self.__year, self.__km, self.__status)

    def get_category(self):
        return self.__category

    def get_lp_number(self):
        return self.__lp_number

    def get_model(self):
        return self.__model

    def get_brand(self):
        return self.__brand

    def get_year(self):
        return self.__year

    def get_km(self):
        return self.__km

    def get_colour(self):
        return self.__colour
    
    def get_status(self):
        return self.__status