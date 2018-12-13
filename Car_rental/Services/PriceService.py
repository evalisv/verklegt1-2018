from repositories.PriceRepo import PriceRepo

class PriceService():
    def __init__(self):
        self.__price_repo = PriceRepo()


    def get_price_list(self):
        print(" ", "{:<15} {:<20} {:<20}".format("Class", "Price per day", "Insurance"))
        print("-"*50)
        for line in self.__price_repo.get_price_list():
            print("  ", "{:<15} {:<20} {:<20}".format(line["Category"], line["Price"], line["Insurance"]))
        return

    def calculate_price(self, class_filter, days_int):
        self.__class_filter = class_filter
        self.__days_int = days_int
        price_list = self.__price_repo.get_price_list()
        vat = float(1.24)
        insurance = int(1200)
        total_price = ""
        for line in price_list:
            if line["Category"] == class_filter:
                price = line["Price"]
                price_int = int(price)
                total_price = price_int * days_int
                total_price_with_vat = (total_price * vat)
                total_price_with_insurance = (total_price_with_vat + insurance)
        print()
        print(" Price without VAT: ", total_price, "ISK")
        print(" Price with VAT: ", total_price_with_vat, "ISK")
        print(" Total price with insurance: ", total_price_with_insurance, "ISK")
        return
        



    def change_price(self, key, key_filter,class_filter):
        self.__class_filter = class_filter
        self.__key = key
        self.__key_filter = key_filter
        match_value = 1
        price_list = self.__price_repo.get_price_list()
        for line in price_list:
            
            if line[key_filter] == class_filter:
                print(" Information to be changed:", line[key])
                new_value = input(" Correct information: ")
                line[key] = new_value
                match_value += 1
                
        if match_value == 1:
            # Notify that something wasn't found
            print(" No class found")

        if match_value != 1:
            self.__price_repo.change_price(price_list)
            print(" Success! Prices changed")

        pass
                

