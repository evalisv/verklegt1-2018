from repositories.PriceRepo import PriceRepository

class PriceService():
    def __init__(self):
        self.__price_repo = PriceRepository()


    def get_price_list(self):
        print(" ", "{:<15} {:<20} {:<20}".format("Class", "Price per day", "Insurance"))
        print("-"*50)
        for line in self.__price_repo.get_price_list():
            print("  ", "{:<15} {:<20} {:<20}".format(line["Category"], line["Price"], line["Insurance"]))
        return
