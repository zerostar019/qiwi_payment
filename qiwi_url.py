from qiwi_config import SECRET_KEY
from pyqiwip2p import QiwiP2P
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

yes = InlineKeyboardButton(text="Да", callback_data="yes_btn")
no = InlineKeyboardButton(text="Нет", callback_data="no_btn")
yno_kb = InlineKeyboardMarkup().add(yes, no)


ok = InlineKeyboardButton(text="Ok", callback_data="not_ok")
not_ok_kb = InlineKeyboardMarkup().add(ok)

ok = InlineKeyboardButton(text="Ok", callback_data="ok")
ok_kb = InlineKeyboardMarkup().add(ok)


QIWI_PRIV_KEY = SECRET_KEY


p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

def create_bill(comment, amount):
    return p2p.bill(amount=amount, lifetime=10, comment=comment).pay_url

def main(comment):
    new_bill_1 = create_bill(comment=comment, amount=590)
    new_bill_2 = create_bill(comment=comment, amount=990)
    new_bill_3 = create_bill(comment=comment, amount=1990)
    first = InlineKeyboardButton(text="1 тариф - 10₽", url=new_bill_1)
    second = InlineKeyboardButton(text="2 тариф - 50₽", url=new_bill_2)
    third = InlineKeyboardButton(text="3 тариф - 100₽", url=new_bill_3)
    support = InlineKeyboardButton(text="Помощь", callback_data="support")
    main_kb = InlineKeyboardMarkup().add(first, second).add(third, support)

    return main_kb