import csv
from models.Price import Price

class PriceRepository():
    def __init__(self):
        self.__price = []


    def get_price_list(self):
        self.__price = []
        with open ("Data/prices.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)   #Til þess að geta filterað út frá lyklum þarf að nota DictReader
            if self.__price == []:
                for line in csv_reader:
                    self.__price.append(line)

        return self.__price
