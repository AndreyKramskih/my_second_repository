from mailbox import Message

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, Message
from aiogram.filters import Command

BOT_TOKEN='7656570135:AAHAU-5sKUFNc5UfgpBqEd4fxrKQWcQpoeU'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')
    ]

    await bot.set_my_commands(main_menu_commands)

# Этот хэндлер будет срабатывать на команду "/delmenu"
# и удалять кнопку Menu c командами
@dp.message(Command(commands='delmenu'))
async def del_main_menu(message:Message):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "menu" удалена')

# Регистрируем асинхронную функцию в диспетчере,
# которая будет выполняться на старте бота,
dp.startup.register(set_main_menu)
# Запускаем поллинг
dp.run_polling(bot)







