from fastapi import FastAPI
from qiwi_bot import dp, bot
from aiogram import Dispatcher, types, Bot
from qiwi_config import webhook

app = FastAPI()

HOST_URL = webhook

# WEBHOOK
WEBHOOK_PATH = f"/bot"
WEBHOOK_URL = f"{HOST_URL}" + f"{WEBHOOK_PATH}"


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
    print(webhook_info)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    print(telegram_update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.post('/payment')
async def payment_result(request: dict):
    status = request['bill']['status']['value']
    user_id = request['bill']['comment']
    if status == "PAID" and user_id is not None:
        await bot.send_message(chat_id=user_id, text="Оплачено")
    return {"OK": True}

