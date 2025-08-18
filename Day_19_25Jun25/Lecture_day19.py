###############################################
geometry

"""
Модуль по геометричних фігурах
"""
# константи
pi = 3.1415

def get_circle_area(radius):
    """
    Рахує площу круга

    :param radius: [int, float], радіус кола
    :return: float, площа
    """
    return pi * radius**2


def get_circle_length(radius):
    """
    Рахує довжину кола

    :param radius: [int, float], радіус кола
    :return: float, довжина
    """
    return 2 * pi * radius


# тестування
# має запускатсь лише коли запускається файл geometry.py

#print(__name__)  # назва файлу який викликає код

if __name__ == '__main__': # файл запущени через Pycharm
    # запуститься лише якщо не import
    for radius in range(1, 10):
        length = get_circle_length(radius)
        area = get_circle_area(radius)

        print(f"{radius = }, {length = }")
        print(f"{radius = }, {area = }")




#########################################
MAIN

# модулі(бібліотеки, фреймворки)
#int, str, list
# if else for while def

# min()
# sorted()

# # підключення модуля(імпортування модуля)
# import geometry
#
#
# # функція з модуля
# # [назва модуля].[назва функції]
# result = geometry.get_circle_area(10)
#
# print(result)

# # запускається код з файлу geometry.py
# import geometry
#
# # використання функції
# print(geometry.get_circle_area(10))
#
# # використання константи
# print(geometry.pi)
#
# # варіанти імпорту
# # import [назва модуля]
# import geometry
#
# geometry.get_circle_length(10)

# # from [назва модуля] import [щось№1], [щось№2]
# from geometry import get_circle_area, pi
#
# res = get_circle_area(10) # працює
# print(res)
#
# # geometry.get_circle_length() # не працює

# # імпортувати все(НЕ РОБИТИ ТАК)
# # from [назва модуля] import *
#
# from geometry import *
#
# get_circle_area(10)

# шукає файл geometry.py в тій же папці що й main.py
# import geometry # не працює

# import modules.geometry
#
# modules.geometry.get_circle_area(10)

# псевдонім(нова назв для модуля)
# import [назва модуля] as [псевдонім]

# import modules.geometry as gm
#
# gm.get_circle_area(10)

# import modules.geometry as gm
#
# help(gm)  # документація


# # вбудовані модулі
# import time # для роботи з часом
#
# # res = time.time()  # кількість секунд з 1 січня 1970 року, 00:00:00
# #
# # print(res)
#
# # обчислити час виконання коду
#
# # початок вимірювання
# start = time.time()
#
# count = 0
# for i in range(10000000):
#     count += 1
#
# # початок вимірювання
# end = time.time()
#
# # тривалість виконання коду
# duration = end - start
#
# print(f"{duration = } секунд")

# модуль для випадковостей
import random

random.seed(42)  # зерно для генерації випадкових чисел
# 42 -- відсилка до Автостопом по галактиці

colors = ['red', 'green', 'blue']
color = random.choice(colors)
print(color)

print(random.randint(0, 1000))
