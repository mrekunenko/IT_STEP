# Завдання 1
# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def display_info(self):
        print(f"Фігура: Прямокутник")
        print(f"  Ширина: {self.width}")
        print(f"  Висота: {self.height}")
        print(f"  Периметр: {self.get_perimeter()}")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        print(f"Фігура: Коло")
        print(f"  Радіус: {self.radius}")
        print(f"  Периметр: {self.get_perimeter():.2f}")


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def display_info(self):
        print(f"Фігура: Трикутник")
        print(f"  Сторони: {self.a}, {self.b}, {self.c}")
        print(f"  Периметр: {self.get_perimeter()}")


def create_figure():




# Завдання 2
# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька співробітників, добавте їх у список та для
# кожного викличте відповідні методи.


# Завдання 3
# Створіть наступні класи:
#  Car – атрибути speed
#  Bicycle – атрибути speed
#  Boat – атрибути speed
# Методи:
#  move() – виводить повідомлення про рух
# o Car – їде по шосе зі швидкістю
# o Bicycle – їде по дорозі зі швидкістю
# o Boat – пливе по воді зі швидкістю
#  check_speed(speed) – перевіряє чи правильна швидкість,
# якщо ні то в __init__ треба викикати ValueError з
# відповідним повідомленням
# o Car – від 20 до 200
# o Bicycle – від 10 до 30
# o Boat – від 0 до 50
# Напишіть функцію create_vehicle() яка запитує у
# користувача тип транспорту та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька транспортних засобів, добавте їх у список
# та для кожної викличте відповідні методи.

class Car:
    def __init__(self, self, speed):
        self.speed = speed
        self.check_speed(speed)

    def move(self):
        print(f"Car їде по шосе зі швидкістю {self.speed} км/год")

    def check_speed(self, speed):
        if not (20 <= speed <= 200):
            raise ValueError("Швидкість машини має бути від 20 до 200")

class Bicycle:
    def __init__(self, speed):
        self.speed = speed
        self.check_speed(speed)

    def move(self):
        print(f"Bicycle їде по дорозі зі швидкістю {self.speed} км/год")

    def check_speed(self, speed):
        if not (10 <= speed <= 30):
            raise ValueError("Швидкість велосипеда має бути від 10 до 30")

class Boat:
    def __init__(self, speed):
        self.speed = speed
        self.check_speed(speed)

    def move(self):
        print(f"Boat пливе по воді зі швидкістю {self.speed} км/год")

    def check_speed(self, speed):
        if not (0 <= speed <= 50):
            raise ValueError("Швидкість човна має бути від 0 до 50")


def create_vehicle():
    vehicle_type = input("Введіть тип транспорту (car / bicycle / boat): ").strip().lower()

    try:
        speed = int(input("Введіть швидкість: ").strip())

        if vehicle_type == "car":
            return Car(speed)
        elif vehicle_type == "bicycle":
            return Bicycle(speed)
        elif vehicle_type == "boat":
            return Boat(speed)
        else:
            print("Невідомий тип транспорту!")
            return None

    except ValueError as e:
        print(f"Помилка: {e}")
        return None







