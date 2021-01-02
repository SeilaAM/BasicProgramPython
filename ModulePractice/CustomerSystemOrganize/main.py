'''
import sys


print('Python Path = ')
for p in sys.path:
    print(p)
'''

from Modules.Asset.BasicData import BasicData
from Modules.System.MemberCard import MemberCard
from Modules.System.Ticket import Ticket

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

# 測試 MemberCard 類別運作正常
print('Member Card Info:')
basic_data = BasicData('John_Smith', '32', 'man', '0900123456', 'john@xmail.com')
member_card = MemberCard(basic_data, '12345678', '2020-01-01', '2025-01-01', 'Normal')
print(member_card.get_member_id())
print(member_card.get_start_date())
print(member_card.get_end_date())
print(member_card.get_member_tiers())
print('\n')

# 測試 Ticket 類別運作正常
print('Ticket Info:')
basic_data = BasicData('John_Smith', '32', 'man', '0900123456', 'john@xmail.com')
ticket = Ticket(basic_data, 'T123456', 'TPEX0001', '2020-01-01', '250')
print(ticket.get_ticket_id())
print(ticket.get_ticket_id())
print(ticket.get_ticket_code())
print(ticket.get_date())
print(ticket.get_price())
