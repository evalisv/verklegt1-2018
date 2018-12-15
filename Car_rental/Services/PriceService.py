from repositories.PriceRepo import PriceRepo

class PriceService():
    def __init__(self):
        self.__price_repo = PriceRepo()


    def get_price_list(self):
        print(20*"-", "Price list", 20*"-")
        print("")
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
        total_price = ""
        for line in price_list:
            if line["Category"] == class_filter:
                price = line["Price"]
                insurance = line["Insurance"]
                price_int = int(price)
                insurance_int = int(insurance)
                total_price = (price_int * days_int)
                total_price_with_vat = int(total_price * vat)
                total_price_with_insurance = int(total_price_with_vat + insurance_int)
        print()
        print(10*"-", "Calculate prices", 10*"-", "\n")
        print(" Price without VAT: ", "{:,d}".format(total_price), "ISK")
        print(" Price with VAT: ", "{:,d}".format(total_price_with_vat), "ISK")
        print(" Total price with insurance: ", "{:,d}".format(total_price_with_insurance), "ISK")
        return None


    def calculate_price_for_order(self, class_filter, days_int, with_insurance):
        self.__class_filter = class_filter
        self.__days_int = days_int
        price_list = self.__price_repo.get_price_list()
        vat = float(1.24)
        total_price = ""
        for line in price_list:
            if line["Category"] == class_filter:
                price = line["Price"]
                insurance = line["Insurance"]
                price_int = int(price)
                insurance_int = int(insurance)
                total_price = (price_int * days_int)
                total_price_with_vat = int(total_price * vat)
                total_price_with_insurance = int(total_price_with_vat + insurance_int)
        if with_insurance in ["Y", "y"]:
            return total_price_with_insurance
        elif with_insurance in ["N", "n"]:
            return total_price_with_vat
        print()
        print(10*"-", "Calculate prices", 10*"-", "\n")
        print(" Price without VAT: ", "{:,d}".format(total_price), "ISK")
        print(" Price with VAT: ", "{:,d}".format(total_price_with_vat), "ISK")
        if insurance in ["Y", "y"]:
            print(" Total price with insurance: ", "{:,d}".format(total_price_with_insurance), "ISK")
        
        



    def change_price(self, key, class_filter):
        self.__class_filter = class_filter
        self.__key = key
        match_value = 1
        price_list = self.__price_repo.get_price_list()
        for line in price_list:
            if line["Category"] == class_filter.upper():
                print(10*"-", "Change Prices", 10*"-", "\n")
                print(" Information to be changed:", line[key])
                new_value = input(" Correct information: ")
                line[key] = new_value
                match_value += 1
                
        if match_value == 1:
            # Notify that something wasn't found
            print(" No class found")

        if match_value != 1:
            self.__price_repo.change_price(price_list)
            print("")
            print(" Success! Prices changed")
            print("")

                

