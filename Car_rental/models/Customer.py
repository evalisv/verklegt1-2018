class Customer:

    def __init__(self, id_number, first_name, last_name, age, country, email, phone, dl_number, cc_number):
        self.__id_number = id_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__country = country
        self.__email = email
        self.__phone = phone
        self.__dl_number = dl_number
        self.__cc_number = cc_number

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(
            self.__id_number, self.__first_name, self.__last_name, self.__age, self.__country, self.__email, self.__phone, self.__dl_number, self.__cc_number)
        
    def get_id_number(self):
        return self.__id_number

    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_age(self):
        return self.__age
    
    def get_country(self):
        return self.__country

    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_dl_number(self):
        return self.__dl_number

    def get_cc_number(self):
        return self.__cc_number
