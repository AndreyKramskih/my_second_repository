from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup,ReplyKeyboardRemove

# Импортируем ReplyKeyboardBuilder из aiogram.utils.keyboard
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from numpy.ma.core import resize

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN='7656570135:AAHAU-5sKUFNc5UfgpBqEd4fxrKQWcQpoeU'

# Создаем объекты бота и диспетчера
bot=Bot(BOT_TOKEN)
dp=Dispatcher()

# Инициализируем объект билдера
kp_builder=ReplyKeyboardBuilder()

# ССоздаем первый список с кнопками
buttons_1: list[KeyboardButton]=[KeyboardButton(text=f'Кнопка {i+1}') for i in range(10)]


#Распаковываем список с кнопками методом add
kp_builder.add(*buttons_1)


# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах,
# а также говорим методу повторять такое размещение для остальных рядов
kp_builder.adjust(1, 2, repeat=True)


# Методом as_markup() передаем клавиатуру как аргумент туда, где она требуется

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text='Чего кошки бояться больше?',
                         reply_markup=kp_builder.as_markup(resize_keyborad=True)
                         )

# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(F.text=='Кнопка 1')
async def process_dog_answer(message:Message):
    await message.answer(
                         text='Да, несомненно, кошки боятся собак. '
                              'Но вы видели как они боятся огурцов?',
                         reply_markup=ReplyKeyboardRemove()
                         )

# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(F.text=='Кнопка 2')
async def process_cucumber_answer(message:Message):
    await message.answer(
                         text='Да, иногда кажется, что огурцов '
                          'кошки боятся больше',
                          reply_markup=ReplyKeyboardRemove()
                         )

if __name__== '__main__':
    dp.run_polling(bot)









