# ----------------- 客戶的基本資料 ----------------- #
class BasicData:
    def __init__(self, name, age, gender, phone, email):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__phone = phone
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email
