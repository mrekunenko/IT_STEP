# Завдання 1
# Напишіть функцію для обрахунку температури склянки води, яку помістили в холодильник через деякий час.
# Параметри:
# T_env – температура в холодильнику
# T0 – початкова температура води
# t – час у секундах проведений в холодильнику
# k – коефіцієнт охолодження, за замовчуванням 0.05
# Формула для обрахунку:
#  ( ) ( )
# Див math.exp()

import math


def water_temperature(T_env, T0, t, k=0.05):
    """
    Обчислює температуру води через t секунд у холодильнику.

    :param T_env: температура в холодильнику
    :param T0: початкова температура води
    :param t: час у секундах
    :param k: коефіцієнт охолодження (за замовчуванням 0.05)
    :return: температура води через t секунд
    """
    return T_env + (T0 - T_env) * math.exp(-k * t)


T_env = float(input("Введіть температуру в холодильнику (T_env): "))
T0 = float(input("Введіть початкову температуру води (T0): "))
t = float(input("Введіть час у секундах (t): "))

# Виклик функції
result = water_temperature(T_env, T0, t)

print(f"Температура води через {t} секунд: {result:.2f}°C")



# Завдання 2
# Напишіть функцію з параметром show_time, яка запитує в
# користувача ім’я та повертає його.
# Якщо show_time = True, то функція повинна вивести на
# екран час своєї роботи у секундах.
# Див time.time()

import time


def get_username(show_time=False):
    """
    Запитує ім’я користувача. Якщо show_time=True — виводить час виконання.

    :param show_time: bool, чи показувати час роботи функції
    :return: str, ім’я користувача
    """
    start = time.time()

    name = input("Введіть ваше ім’я: ")

    end = time.time()

    if show_time:
        print(f"Час виконання: {end - start:.4f} секунд")

    return name


# Варіант без виведення часу
user_name = get_username()
print(f"Привіт, {user_name}!")

# Варіант з виведенням часу
user_name = get_username(show_time=True)
print(f"Привіт, {user_name}!")



# Завдання 3
# Напишіть власний модуль date_utils.py з функцією яка
# отримує дату дедлайну у форматі YYYY-MM-DD. Поверніть
# кількість днів яка залишилаь до дедлайна.
# Імпортуйте цей модуль в іншому файлі та використайте
# функцію, дедлайн вводить користувач. Якщо залишилось
# менше тижня до кінця дедлайна, виведіть відповідне
# повідомлення.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days

# 1. Файл date_utils.py
from datetime import date

def days_until_deadline(deadline_str):
    """
    Рахує кількість днів до дедлайну.

    :param deadline_str: рядок у форматі YYYY-MM-DD
    :return: кількість днів до дедлайну
    """
    deadline = date.fromisoformat(deadline_str)
    today = date.today()
    delta = deadline - today
    return delta.days


# 2. Головний файл main.py
import date_utils

# Введення користувачем дати дедлайну
deadline_input = input("Введіть дату дедлайну (YYYY-MM-DD): ")

# Виклик функції з модуля
days_left = date_utils.days_until_deadline(deadline_input)

# Вивід результату
print(f"До дедлайну залишилось {days_left} днів.")

if days_left < 7 and days_left >= 0:
    print("Увага! Менше тижня до дедлайну!")
elif days_left < 0:
    print("Дедлайн вже минув!")
