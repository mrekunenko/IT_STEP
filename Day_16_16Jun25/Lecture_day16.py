# if isupper:

# # Завдання 1
# # Напишіть функцію, яка буде приймати на вхід три числа
# # в якості параметрів і повертати їх медіану. В основній програмі
# # повинен виконуватися запит до користувача на предмет введення
# # трьох чисел, а також виклик функцій і відображення результату.
#
# def get_median(num1, num2, num3):
#     # код функції
#
#     # треба відсортувати 3 числа
#     nums = [num1, num2, num3]
#     nums.sort()
#
#     # дістати медіану
#     median = nums[1]
#
#     return median
#
#
# # основна програма
#
#
# num1 = int(input("Введіть число 1: "))
# num2 = int(input("Введіть число 2: "))
# num3 = int(input("Введіть число 3: "))
#
# # виклик функції
# median = get_median(num1, num2, num3)
#
# # відображення результату
# print(f"Медіана -- {median}")


# # про return
#
# def func():
#     num = 2 + 3
#
#     return num
#
#     print('щось після return')
#
#
# def func1():
#     for i in range(1, 10):
#         print(i)
#         if i == 5:
#             return 'Кінець'
#
#     print('код після циклу')
#
#
# res = func1()
# print(res)









# напишіть функцію яка знаходить перше додатнє число в списку.
# список передається як параметр. функція має повернути
# перше додатнє число, або none якщо такого немає


# def get_positive(nums):
#     for num in nums:
#         if num > 0:
#             return num  # функція припиняє роботу
#
#     return None
#
#
# def func():
#     num = 2+2  # буде return None
#
#
# #nums = [-1, 0, -2, 5, 6, -8]
# nums = [-1, -2, -3, -2, -5]
#
# print(get_positive(nums))

# напишіть функцію яка перевіряє чи всі числа в списку додатні.

# def check_positive(nums):
#     for num in nums:
#         # якщо є хоча б одне від'ємне то результат False
#         if num < 0:
#             return False
#
#     # функція продовжує працювати
#     return True
#
#
# #nums = [-1, 0, -2, 5, 6, -8]
# #nums = [-1, -2, -3, -2, -5]
# nums = [1, 2, 3, 4, 5]
#
# print(check_positive(nums))

# def func():
#     return 2
#     print('hjkllhj')
#     return "next"
#
#
# print(func())


# пам'ять

# глобальна область видимості

# def func(data):
#     # data -- локальна змінна
#     # локальна область видимості
#     text = 'hello'
#
#     word = 'banana'  # локальна змінна
#
#     data += 1
#
#     # print(text)  # локальна змінна
#     # print(num)   # глобальна змінна
#     # # як глобальні змінні у функціях використровують константи
#
#     return 10
#
#
# num = 5  # глобальна змінна
# word = 'apple'  # глобальна змінна
# data = 123
#
# res = func(data)
#
# print(word)
#
# # print(num)
# # print(text)

# def func(nums):
#     # шоб список в глобалтній області не змінився
#     # робимо копію
#     # nums = nums.copy()
#
#     # nums.append(100)
#     nums = [-100, 2, 3]
#     return nums
#
#
# nums = [1, 2, 3]
#
# new_nums = func(nums)
#
# print(nums)




# напишіть функцію, яка множить всі від’ємні числа на 2 зі
# списку. список передається як параметр. функція має
# повернути кількість змінених чисел.


# def double_negative(nums):
#     counter = 0
#
#     for i in range(len(nums)):
#         if nums[i] < 0:
#             nums[i] *= 2
#             counter += 1
#
#     return counter
#
#
# data = [-1, 2, -3, -4, 5]
# count = double_negative(data)
#
# print(data)
# print(count)




# напишіть функцію, яка видаляє всі числа 7 зі
# списку. список передається як параметр. функція має
# повернути кількість видалених чисел.


# # варіант 1
# def remove7(nums):
#     new_nums = []
#
#     for num in nums:
#         if num != 7:
#             new_nums.append(num)
#
#     return new_nums
#
#
# data = [1, 2, 7, 7, 3, 4, 7]
#
# data = remove7(data)
#
# print(data)

# варіант 2
data = [1, 2, 7, 7, 3, 4, 7]

# data[4] = 100
# print(data)

# data[2:4] = [1, 2, 3, 4, 5, 6, 7, 8]
# print(data)

# data[:] = [1, 2, 3]
# print(data)

def remove7(nums):
    new_nums = []

    for num in nums:
        if num != 7:
            new_nums.append(num)

    nums[:] = new_nums


data = [1, 2, 7, 7, 3, 4, 7]

remove7(data)

print(data)