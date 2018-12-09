from Services.CarService import CarService
from models.Car import Car

class CarUi():

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("You can do the following: ")
            print("1 | See available cars")
            print("2 | See list of all cars")
            print("3 | Car status")
            print("4 | Register new car")
            print("b | To go back")
            print("m | to go to main menu")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "4":
                lp_number = input("Licence plate: ")
                category = input("Category: ")
                model = input("Model: ")
                brand = input("Brand: ")
                colour = input("Colour: ")
                year = input("Year: ")
                km = input("Kilometers: ")
                status = input("Status: ")
                new_car = Car(category, lp_number, model, brand, year, km, colour, status)
                self.__car_service.add_car(new_car)

            elif action == "2":
                videos = self.__video_service.get_videos()
                print(videos)
                    