from aiogram import Dispatcher, Bot, types
from qiwi_config import BOT_API_TOKEN
from qiwi_url import yno_kb, not_ok_kb, ok_kb, main

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Вам исполнилось 18 (восемнадцать) лет?", reply_markup=yno_kb)


@dp.callback_query_handler(lambda call: call.data == "yes_btn")
async def send_payment_links(callback: types.CallbackQuery):
    await callback.answer(cache_time=10)
    pay_kb = main(comment=callback.from_user.id)
    await callback.message.edit_text(text="Купи приватный доступ, чтобы увидеть больше", reply_markup=pay_kb)


@dp.callback_query_handler(lambda call: call.data == "no_btn")
async def send_reject(callback: types.CallbackQuery):
    await callback.answer(cache_time=10)
    await callback.message.edit_text(text="К сожалению, мы не можем открыть доступ несовершеннолетним!", reply_markup=not_ok_kb)


@dp.callback_query_handler(lambda call: call.data == "support")
async def send_support(callback: types.CallbackQuery):
    await callback.answer(cache_time=10)
    await callback.message.edit_text(text="Чтобы получить ответы на все Ваши вопросы, пишите - @botfather", reply_markup=ok_kb)


@dp.callback_query_handler(lambda call: call.data == "not_ok")
async def start_(callback: types.CallbackQuery):
    await callback.answer(cache_time=10)
    await callback.message.edit_text(text="Вам исполнилось 18 (восемнадцать) лет?", reply_markup=yno_kb)


@dp.callback_query_handler(lambda call: call.data == "ok")
async def start_(callback: types.CallbackQuery):
    await callback.answer(cache_time=10)
    pay_kb = main(comment=callback.from_user.id)
    await callback.message.edit_text(text="Купи приватный доступ, чтобы увидеть больше", reply_markup=pay_kb)

