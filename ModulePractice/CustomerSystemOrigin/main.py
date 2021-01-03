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


# ------------------- 定義會員卡 ------------------ #
class MemberCard:
    def __init__(self, basic_data, member_id, start_date, end_date, member_tiers):
        self.__basic_data = basic_data
        self.__member_id = member_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__member_tiers = member_tiers

    def get_basic_data(self):
        return self.__basic_data

    def get_member_id(self):
        return self.__member_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_member_tiers(self):
        return self.__member_tiers

    def set_basic_data(self, basic_data):
        self.__basic_data = basic_data

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_member_tiers(self, member_tiers):
        self.__member_tiers = member_tiers


# 將會員卡資料加入對應的資料庫的函式
def add_data(new_member):
    print('Add member card data to database')


def remove_data(member_id):
    print('Remove member card data from database')


def search_data(member_id):
    print('Search member card data in database')


# -------------------- 定義票卷 -------------------- #
class Ticket:
    def __init__(self, basic_data, ticket_id, ticket_code, date, price):
        self.__basic_data = basic_data
        self.__ticket_id = ticket_id
        self.__ticket_code = ticket_code
        self.__date = date
        self.__price = price

    def get_basic_data(self):
        return self.__basic_data

    def get_ticket_id(self):
        return self.__ticket_id

    def get_ticket_code(self):
        return self.__ticket_code

    def get_date(self):
        return self.__date

    def get_price(self):
        return self.__price

    def set_basic_data(self, basic_data):
        self.__basic_data = basic_data

    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id

    def set_ticket_code(self, ticket_code):
        self.__ticket_code = ticket_code

    def set_date(self, date):
        self.__date = date

    def set_price(self, price):
        self.__price = price


# 將票卷資料加入對應的資料庫的函式
def add_data(new_member):
    print('Add ticket data to database')


def remove_data(member_id):
    print('Remove ticket data from database')


def search_data(member_id):
    print('Search ticket data in database')


print('\n')
# ---------- 測試 BasicData 類別運作正常 ---------- #
basic_data = BasicData('John', '32', 'man', '0900123456', 'john@xmail.com')
print('[Original Basic Data]')
print('Name = ' + basic_data.get_name())
print('Age = ' + basic_data.get_age())
print('Gender = ' + basic_data.get_gender())
print('Phone = ' + basic_data.get_phone())
print('Email = ' + basic_data.get_email())
print('\n')

# 測試 BasicData 類別中用來修改資料的方法
basic_data.set_name('John Smith')
basic_data.set_age('99')
basic_data.set_gender('mana')
basic_data.set_phone('0988765432')
basic_data.set_email('john_smith@xmail.com.tw')

print('[Modified Basic Data]')
print('Name = ' + basic_data.get_name())
print('Age = ' + basic_data.get_age())
print('Gender = ' + basic_data.get_gender())
print('Phone = ' + basic_data.get_phone())
print('Email = ' + basic_data.get_email())
print('\n')

# 測試 MemberCard 類別運作正常
print('[Member Card Info]')
basic_data = BasicData('John_Smith', '32', 'man', '0900123456', 'john@xmail.com')
member_card = MemberCard(basic_data, '12345678', '2020-01-01', '2025-01-01', 'Normal')
print(member_card.get_member_id())
print(member_card.get_start_date())
print(member_card.get_end_date())
print(member_card.get_member_tiers())
print('\n')

# 測試 Ticket 類別運作正常
print('[Ticket Info]')
basic_data = BasicData('John_Smith', '32', 'man', '0900123456', 'john@xmail.com')
ticket = Ticket(basic_data, 'T123456', 'TPEX0001', '2020-01-01', '250')
print(ticket.get_ticket_id())
print(ticket.get_ticket_id())
print(ticket.get_ticket_code())
print(ticket.get_date())
print(ticket.get_price())
