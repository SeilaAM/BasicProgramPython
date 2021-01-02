from ..Asset.BasicData import BasicData


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


if __name__ == '__main__':
    # 測試 MemberCard 類別運作正常
    print('Member Card Info:')
    basic_data = BasicData('John_Smith', '32', 'man', '0900123456', 'john@xmail.com')
    member_card = MemberCard(basic_data, '12345678', '2020-01-01', '2025-01-01', 'Normal')
    print(member_card.get_member_id())
    print(member_card.get_start_date())
    print(member_card.get_end_date())
    print(member_card.get_member_tiers())
    print('\n')
