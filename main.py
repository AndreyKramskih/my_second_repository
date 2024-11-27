import logging
import sys

# Определяем первый вид форматирования
format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
           '%(lineno)d - %(name)s - %(message)s'
# Определяем второй вид форматирования
format_2 = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'

# Инициализируем первый форматтер
format_1=logging.Formatter(fmt=format_1)
# Инициализируем второй форматтер
format_2=logging.Formatter(fmt=format_2, style='{')

# Создаем логгер
logger=logging.getLogger(__name__)

# Инициализируем хэндлер, который будет перенаправлять логи в stderr
stderr_handler=logging.StreamHandler()
# Инициализируем хэндлер, который будет перенаправлять логи в stdout
stdout_handler=logging.StreamHandler(sys.stdout)

# Устанавливаем форматтеры для хэндлеров
stderr_handler.setFormatter(format_1)
stdout_handler.setFormatter(format_1)

# Добавляем хэндлеры логгеру
logger.addHandler(stderr_handler)
logger.addHandler(stdout_handler)

# Создаем лог
logger.warning('Это лог с предупреждением')







