from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN='7656570135:AAHAU-5sKUFNc5UfgpBqEd4fxrKQWcQpoeU'
bot=Bot(BOT_TOKEN)
dp=Dispatcher()
kp_builder=ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn=KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn=KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn=KeyboardButton(
    text='Созадать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)
web_app_btn=KeyboardButton(
    text='Start Wep App',
    web_app=WebAppInfo(url='https://www.vseinstrumenti.ru/')
)
# Добавляем кнопки в билдер
kp_builder.row(contact_btn, geo_btn, poll_btn, web_app_btn,  width=1)

# Создаем объект клавиатуры
keyboard:ReplyKeyboardMarkup=kp_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(
        text='Экспериментируем с кнопками',
        reply_markup=keyboard
    )

# Этот хэндлер будет срабатывать на команду "/web_app"
@dp.message(Command(commands='web_app'))
async def process_web_app_command(message:Message):
    await message.answer(
        text='Идем в Систерм',
        reply_markup=keyboard
    )



if __name__== '__main__':
    dp.run_polling(bot)









