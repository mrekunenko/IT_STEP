# Завдання 1
# Напишіть функцію, яка повертає суму чисел з
# списку. Список передається як параметр.

def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [1, 2, 3, 4, 5]
result = sum_numbers(my_list)
print(result)


# Завдання 2
# Напишіть функцію, яка повертає найбільше число з
# списку. Список передається як параметр.

def find_max(numbers):
    return max(numbers)

my_list = [3, 7, 2, 9, 1, 5]
result = find_max(my_list)
print(result)


# Завдання 3
# Напишіть функцію, яка повертає кількість простих чисел з
# списку. Список передається як параметр.
# Для цього завдання вам потрібно написати функцію, яка
# отримує число як параметр, та повертає True якщо воно
# просте, та False в протилежному випадку.

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(count_primes(numbers))


# Завдання 4
# Напишіть функцію, яка видаляє всі від’ємні числа зі
# списку. Список передається як параметр. Функція має
# повернути кількість видалених чисел.

def remove_negatives(numbers):
    count = 0
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            numbers.pop(i)
            count += 1
        else:
            i += 1
    return count

nums = [1, -2, 3, -4, 5]
removed = remove_negatives(nums)
print(nums)
print(removed)


# Завдання 5
# Напишіть функцію, яка шукає певне число в списку.
# Функція повинна повертати список усіх індексів цього
# числа в списку. Якщо числа немає в списку, то потрібно
# повернути порожній список. Список та число
# передаються як два параметри.


def find_indexes(numbers, target):
    indexes = []
    for i in range(len(numbers)):
        if numbers[i] == target:
            indexes.append(i)
    return indexes

user_input = input("Введіть числа через пробіл: ")
number_list = []
for x in user_input.split():
    number_list.append(int(x))

target = int(input("Яке число шукаєте в списку? "))

result = find_indexes(number_list, target)

if result:
    print("Число на позиціях:", result)
else:
    print("Число не знайдене.")


# Завдання 6
# Напишіть функцію, рахує факторіал кожного
# елемента списку. Результатом має бути список з
# факторіалами.
# Факторіалом числа n (позначають n!) називаю
# добуток усіх чисел від 1 до n. Наприклад 6! =
# 1*2*3*4*5*6. Якщо число від’ємне, то вважайте що
# його фактор

def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def list_factorials(numbers):
    return [factorial(num) for num in numbers]

numbers = [3, 5, -2, 0, 6]
result = list_factorials(numbers)
print(result)