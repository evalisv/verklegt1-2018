import csv
from models.Price import Price

class PriceRepo:
    def __init__(self):
        self.__price = []


    def get_price_list(self):
        self.__price = []
        with open ("data/prices.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)   #Til þess að geta filterað út frá lyklum þarf að nota DictReader
            if self.__price == []:
                for line in csv_reader:
                    self.__price.append(line)

        return self.__price

    def change_price(self, new_value):
        self.__new_value = new_value
        with open ("data/prices.csv", "w", encoding = "utf-8") as changed_csv:
            fieldnames = ["Class", "Price", "Insurance"]
            csv_writer = csv.DictWriter(changed_csv, fieldnames = fieldnames, lineterminator = "\n")
            csv_writer.writeheader()
            for line in new_value:
                csv_writer.writerow(line)

        