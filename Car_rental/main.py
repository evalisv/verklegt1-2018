import csv
from ui.EmployeeUi import EmployeeUi

access = ""

def login():
    print('Please sign in')
    with open("Data/users.csv", encoding="utf-8") as csvfile:
        database = csv.DictReader(csvfile)
        loggedin = False
        while loggedin is not True:
            Username = input('Username: ')
            Password = input('Password: ')
            for row in database:
                Username_File = row['username']
                Password_File = row['password']
                user_access = row['access']
                if (Username_File == Username and
                    Password_File == Password and
                        user_access == 'user'):
                    loggedin = True
                    print('Succesfully logged in.')
                    return user_access
                    # patientmenu()  # we will add this later on
                if (Username_File == Username and
                    Password_File == Password and
                        user_access == 'admin'):
                    loggedin = True
                    print('Succesfully logged in as an admin.')
                    return user_access
                    # artsmenu()     # we will add this later on
                if loggedin == False:
                    print('wrong username or password')
    

def main():
    
    ui = EmployeeUi()
    ui.main_menu()

    # get_login = login()
    # if get_login == "user":
    #     ui = EmployeeUi()
    #     ui.main_menu()
    # elif get_login =="admin":
    #     #Hér á að breyta því að admin fái aðgang að admin ui sem verður með fleiri breytum.
    #     ui = EmployeeUi()
    #     ui.main_menu()

main()
    



#Hér keyrum við main fallið til að ræsa forritið.
# def main():
#     carui = CarUi()
#     carui.main_menu()

# main()
    #tilraunastarfsemi í meira lagi


# Virkar ekki, þurfum mögulega að hafa eina risastóra UI skrá.
# def main_menu():
    
#         action = ""
#         while(action != "q"):
#             print("You can do the following:")
#             print()
#             print("1 | Cars")
#             print("2 | Orders")
#             print("3 | Customers")
#             print("q | Quit")
#             print()

#             action = input("Input number/letter: ").lower

#             if action == "3":
#                 customer_ui = CustomerUI()
#                 customer_ui.main_menu()
#                 continue
                
#             elif action == "1":
#                 car_ui = CarUi()
#                 car_ui.main_menu()

# main_menu()
