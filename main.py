print(dir())

import functions as f
from data import my_dict
from classes import *

print('Это исполняемый файл')

new_variable:int = 15


if __name__ == '__main__':
    print('Код ниже не выполнится, если этот файл будет импортируемым модулем в другой исполняемый файл')
    print(f.get_double_number(100))
    print(my_dict)
    MyClass()
    print(dir())

