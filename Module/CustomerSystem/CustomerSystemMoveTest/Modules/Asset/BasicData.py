print('BasicData __name__ = ' + __name__ + '\n')


# 客戶的基本資料
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


if __name__ == '__main__':
    # ---------- 測試 BasicData 類別運作正常 ---------- #
    basic_data = BasicData('John', '32', 'man', '0900123456', 'john@xmail.com')
    print('Original Basic Data:')
    print('Name = ' + basic_data.get_name())
    print('Age = ' + basic_data.get_age())
    print('Gender = ' + basic_data.get_gender())
    print('Phone = ' + basic_data.get_phone())
    print('Email = ' + basic_data.get_email())
    print('\n')

    basic_data.set_name('John Smith')
    basic_data.set_age('99')
    basic_data.set_gender('mana')
    basic_data.set_phone('0988765432')
    basic_data.set_email('john_smith@xmail.com.tw')

    print('Modified Basic Data:')
    print('Name = ' + basic_data.get_name())
    print('Age = ' + basic_data.get_age())
    print('Gender = ' + basic_data.get_gender())
    print('Phone = ' + basic_data.get_phone())
    print('Email = ' + basic_data.get_email())
    print('\n')
