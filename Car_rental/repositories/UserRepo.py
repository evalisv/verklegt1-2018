import csv
from models.user import user


class UserRepo():
    def __init__(self):
        self.__user = []

    def add_User(self, user):
        with open('Car_rental/data/users.csv', 'a+', encoding = "utf-8") as order_file:
            staff_name = user.get_staff_name()
            id_number = user.get_id_number() 
            email = user.get_email()
            username = user.get_username()
            password = user.get_password()
            access = user.get_access


            fieldnames = ['staff_name', 'id_number', 'email', 'username', 'password', 'access']

            csv_writer = csv.DictWriter(order_file, fieldnames=fieldnames, lineterminator="\n")
            #Spurning með writeheader. Virðist adda header með hverri nýrri línu.
            csv_writer.writeheader()
            csv_writer.writerow({'staff_name': staff_name , 'id_number': id_number , 'email': email , 'username': username ,
                            'password': password , 'access': access })