class User:

    def __init__(self, staff_name, id_number, email, username, password, access):
        self.__staff_name = staff_name
        self.__id_number = id_number
        self.__email = email
        self.__username = username
        self.__password = password
        self.__access = access

    def __str__(self):
        return "{},{},{},{},{},{}".format(
            self.__staff_name, self.__id_number, self.__email, self.__username, self.__password, self.__access)

    def get_staff_name(self):
        return self.__staff_name

    def get_staff_id_number(self):
        return self.__id_number

    def get_staff_email(self):
        return self.__email
    
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_access(self):
        return self.__access