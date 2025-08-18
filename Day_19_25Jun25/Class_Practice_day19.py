# Завдання 1
# Напишіть власний модуль string_utils.py з наступними функціями:
# a) Видалення знаків пунктуації з рядка: ,.?!;:
# b) Підрахунок кількості голосних у рядку
# c) Перевірка чи є рядок паліндромом(читається однаково задом наперед)
# Імпортуйте цей модуль в іншому файлі та використайте всі 3 функції.
# Додатково у файлі string_utils.py напишіть код перевірки роботи функцій: користувач вводить назву функції та рядок, потрібно вивести результат.
# Ця перевірка не повинна запускатись при імпорті в іншому файлі.


# string_utils.py

vowels = "aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ"
punctuation = ",.?!;:"

def remove_punctuation(text):
    """
    Видаляє знаки пунктуації з рядка
    :param text: str, вхідний рядок
    :return: str, рядок без знаків пунктуації
    """
    result = ""
    for char in text:
        if char not in punctuation:
            result += char
    return result


def count_vowels(text):
    """
    Підраховує кількість голосних у рядку
    :param text: str, вхідний рядок
    :return: int, кількість голосних
    """
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def is_palindrome(text):
    """
    Перевіряє чи є рядок паліндромом
    :param text: str, вхідний рядок
    :return: bool, True якщо паліндром, False якщо ні
    """
    # Очищаємо рядок від пунктуації та пробілів, робимо малими літерами
    cleaned = ""
    for char in text.lower():
        if char.isalpha():
            cleaned += char

    # Перевіряємо чи читається однаково в обох напрямках
    return cleaned == cleaned[::-1]


# # Тестування функцій
# if __name__ == "__main__":
#     print("=== Тестування модуля string_utils ===")
#
#     while True:
#         print("\nДоступні функції:")
#         print("1. remove_punctuation - видалити пунктуацію")
#         print("2. count_vowels - підрахувати голосні")
#         print("3. is_palindrome - перевірити паліндром")
#         print("4. exit - вийти")
#
#         choice = input("Введіть назву функції або номер: ").strip()
#
#         if choice == "exit" or choice == "4":
#             break
#
#         text = input("Введіть рядок для обробки: ")
#
#         if choice == "remove_punctuation" or choice == "1":
#             result = remove_punctuation(text)
#             print(f"Результат: '{result}'")
#
#         elif choice == "count_vowels" or choice == "2":
#             result = count_vowels(text)
#             print(f"Кількість голосних: {result}")
#
#         elif choice == "is_palindrome" or choice == "3":
#             result = is_palindrome(text)
#             print(f"Чи є паліндромом: {'Так' if result else 'Ні'}")
#
#         else:
#             print("Невірна назва функції!")
#
#     print("До побачення!")


# main.py


import string_utils

text = input("Введіть рядок: ")

print("1. Без пунктуації:", string_utils.remove_punctuation(text))
print("2. Кількість голосних:", string_utils.count_vowels(text))
print("3. Це паліндром?:", string_utils.is_palindrome(text))



# Завдання 2
# Напишіть функцію для обрахунку площі трикутника по формулі S= 0.5*a*b*sin(y) - Площа трикутника дорівнює половині добутку двох його сторін і синуса кута між ними.
# Параметри функції: сторони a і b та кут (y). Функцію синус візьміть з модуля math.
# Примітка: якщо ви будете вводити кут у градусах, то
# перед тим як рахувати синус, його потрібно перевести у
# радіани.
# math.radians()

import math


def triangle_area(a, b, angle_degrees):
    """
    Обчислює площу трикутника за формулою: S = 0.5 * a * b * sin(y)
    де a, b - сторони трикутника, y - кут між ними у градусах

    :param a: float, перша сторона трикутника
    :param b: float, друга сторона трикутника
    :param angle_degrees: float, кут між сторонами у градусах
    :return: float, площа трикутника
    """
    # Переводимо кут з градусів у радіани
    angle_radians = math.radians(angle_degrees)

    # Обчислюємо площу
    area = 0.5 * a * b * math.sin(angle_radians)

    return area


# Приклад використання функції
if __name__ == '__main__':
    # Тестові дані
    side_a = 5.0
    side_b = 7.0
    angle = 30  # градусів

    # Обчислення площі
    result = triangle_area(side_a, side_b, angle)
    print(f"Площа трикутника зі сторонами {side_a} і {side_b} та кутом {angle}°: {result:.2f}")



# Завдання 3
# Напишіть функцію, яка обчислює суму чисел від 1 до 10
# млн. Виведіть час роботи програми.
# Див time.time()

import time

def sum_to_ten_million():
    """
    Обчислює суму чисел від 1 до 10_000_000
    та виводить час виконання.
    """
    start = time.time()  # Початок вимірювання

    total = 0
    for i in range(1, 10_000_001):
        total += i

    end = time.time()  # Кінець вимірювання
    duration = end - start

    print(f"Сума: {total}")
    print(f"Час виконання: {duration:.4f} секунд")

# Виклик функції
sum_to_ten_million()




# Завдання 4
# Користувач вводить свою дату народження у форматі
# YYYY-MM-DD. Виведіть вік користувача.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days


import datetime

def calculate_age():
    """
    Обчислює вік користувача за датою народження у форматі YYYY-MM-DD.
    """
    birth_str = input("Введіть дату народження (YYYY-MM-DD): ")
    birth_date = datetime.date.fromisoformat(birth_str)
    today = datetime.date.today()

    # Різниця у днях
    delta = today - birth_date
    age_years = delta.days // 365  # наближено, без врахування високосних років

    print(f"Ваш вік: {age_years} років")

# Виклик функції
calculate_age()
