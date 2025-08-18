# Завдання 1
# Напишіть lambda-функції, які:
# 1. Підносить число до квадрату
# 2. Отримує довжини трикутника і повертає периметр
# 3. Отримує прізвище та ім’я і повертає рядок у форматі «Прізвище, ім’я»
# 4. Перевіряє чи є число парним

# 1. Квадрат числа
square = lambda x: x ** 2

# 2. Периметр трикутника (довжини трьох сторін)
perimeter = lambda a, b, c: a + b + c

# 3. Форматування ПІБ
format_name = lambda last, first: f"{last}, {first}"

# 4. Перевірка на парність
is_even = lambda x: x % 2 == 0


# === Приклад використання з введенням ===

# 1. Квадрат
x = int(input("Введи число: "))
print("Квадрат:", square(x))

# 2. Периметр
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))
print("Периметр трикутника:", perimeter(a, b, c))

# 3. ПІБ
last = input("Прізвище: ")
first = input("Ім’я: ")
print("Форматовано:", format_name(last, first))

# 4. Парність
num = int(input("Введи число: "))
print("Парне?" , is_even(num))


# Завдання 2
# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел та повертає список з лише
# додатніми числами
#  Отримує список слів та повертає список слів, в яких
# більше ніж 3 літери
#  Отримує список слів та літеру і повертає список тих
# слів, які починаються на цю літеру(регістр
# неважливий)

# 1. Повертає лише додатні числа
def filter_positive(nums):
    return list(filter(lambda x: x > 0, nums))

# 2. Повертає слова з більше ніж 3 літерами
def filter_long_words(words):
    return list(filter(lambda word: len(word) > 3, words))

# 3. Повертає слова, які починаються на задану літеру (нечутливо до регістру)
def filter_by_letter(words, letter):
    return list(filter(lambda word: word.lower().startswith(letter.lower()), words))


# === Приклад використання з введенням ===

# 1. Додатні числа
nums = list(map(int, input("Введи числа через пробіл: ").split()))
print("Додатні:", filter_positive(nums))

# 2. Слова з більше ніж 3 літер
words = input("Введи слова через пробіл: ").split()
print("Слова > 3 літери:", filter_long_words(words))

# 3. Слова на певну літеру
letter = input("Введи літеру: ")
print("Слова на літеру:", filter_by_letter(words, letter))


# Завдання 3
# Напишіть функцію, яка отримує іншу функцію та
# параметри. Поверніть час роботи функції у секундах

import time

def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print("Результат:", result)
    return end - start


# === Приклад використання з введенням ===

# Функція для прикладу — обчислення суми від 1 до n
def calculate_sum(n):
    return sum(range(1, n + 1))

# Введення числа
n = int(input("Введи число n: "))
execution_time = measure_time(calculate_sum, n)
print("Час виконання:", execution_time, "секунд")



# Завдання 4
# Напишіть функції, які:
#  Сортує список слів за останньою літерою
#  Сортує список чисел за кількістю цифр
#  Знаходить число зі списку, яке найближче до
# заданого(передається як параметр)
#  Знаходить слово у списку з найменшою довжиною
#  Сортує список чисел за кількістю цифр, якщо кількість
# цифр однакова, то сортує за значенням числа


# 1. Сортує слова за останньою літерою
def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1])

# 2. Сортує числа за кількістю цифр
def sort_by_digit_count(nums):
    return sorted(nums, key=lambda num: len(str(abs(num))))

# 3. Знаходить число, найближче до заданого
def closest_to_target(nums, target):
    return min(nums, key=lambda num: abs(num - target))

# 4. Найкоротше слово у списку
def shortest_word(words):
    return min(words, key=len)

# 5. Сортує за кількістю цифр, потім за значенням
def sort_by_digits_then_value(nums):
    return sorted(nums, key=lambda num: (len(str(abs(num))), num))


# Ввід
words = input("Введи слова через пробіл: ").split()
nums = list(map(int, input("Введи числа через пробіл: ").split()))
target = int(input("Введи число для пошуку найближчого: "))

# Виклики
print("1. Сортування за останньою літерою:", sort_by_last_letter(words))
print("2. Сортування за кількістю цифр:", sort_by_digit_count(nums))
print("3. Найближче до", target, ":", closest_to_target(nums, target))
print("4. Найкоротше слово:", shortest_word(words))
print("5. Сортування за цифрами, потім значенням:", sort_by_digits_then_value(nums))
