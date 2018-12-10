from UI.CarUI import CarUi
from UI.CustomerUI import CustomerUI
#Hér keyrum við main fallið til að ræsa forritið.
# def main():
#     carui = CarUi()
#     carui.main_menu()

# main()
    #tilraunastarfsemi í meira lagi


# Virkar ekki, þurfum mögulega að hafa eina risastóra UI skrá.
def main_menu():
    
        action = ""
        while(action != "q"):
            print("You can do the following:")
            print()
            print("1 | Cars")
            print("2 | Orders")
            print("3 | Customers")
            print("q | Quit")
            print()

            action = input("Input number/letter: ").lower

            if action == "3":
                customer_ui = CustomerUI()
                customer_ui.main_menu()
                continue
                
            elif action == "1":
                car_ui = CarUi()
                car_ui.main_menu()

main_menu()
