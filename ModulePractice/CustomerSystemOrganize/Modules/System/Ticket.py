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
