# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

import logging
import sys

LogFormat = '%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('Task1error', 'a', 'utf-8')
formatter = logging.Formatter(LogFormat)
handler.setFormatter(formatter)
logger.addHandler(handler)

def inputRequest(rep = 3):
    while True:
        if rep == 0:
            print("Количество попыток истекло")
            logger.error(f'Количество попыток истекло')
            break
        num = input('Введите вещественное число: ')
        try:
            num = float(num)
            logger.info(f'Введено число: {num}')
            return num
        except:
            logger.error(f'Некорректный ввод: {num}')
            print("Некорректный ввод, попробуйте еще раз")
            rep -= 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            var = int(sys.argv[1])
        except:
            print("некорректный параметр, будет использовно значение количества попыток по умолчанию 3")
            var = 3
    else:
        var = 3
    inputRequest(var)

# (venv) PS C:\Users\Миша\PycharmProjects\pythonProject> python Homework15.py 5
# (venv) PS C:\Users\Миша\PycharmProjects\pythonProject> python Homework15.py
# (venv) PS C:\Users\Миша\PycharmProjects\pythonProject> python Homework15.py 5 4 8
# (venv) PS C:\Users\Миша\PycharmProjects\pythonProject> python Homework15.py яблоко


