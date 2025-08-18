# декоратори

# функція як об'єкт

def func():
    num = 10

    print("hello")

    return 5

text = 'start'

# # присвоєння
# # new_func --  це те що в return
# new_func = func()
#
# print(new_func)
#
# # new_func --  це саме функція func
# new_func = func
# print(new_func)
#
# # new_func = func
# #
# # new_func()
# #
# # my_print = print
# # my_print(1, 2, 3, sep=' ')
# #
# # # func = 2
# # # func()
# #
# # # ось так ви втрачаєте доступ до функцій
# # min = 10
# # str = 'jkl'


# # список функцій
# def mean(num1, num2):  # середнє арифметичне
#     return (num1 + num2) / 2
#
#
# # список функцій
# funcs = [min, max, mean]
#
# for func in funcs:
#     result = func(10, 20)
#
#     # назва функції
#     name = func.__name__
#
#     print(f"{name}(10, 20) = {result}")


# функція як аргумент(параметр) іншої функція

# def func(num, text):
#     print(f"{num}, {text}")
#
#
# func(1, 'text')

# функція яка застосовує іншу функцію до 10, 20
# def apply_func(func):
#     result = func(10, 20)
#     print(result)
#     return result
#
#
# apply_func(max)

# отримати найкоротше слово зі списку слово

words = ['apple', 'banana', 'cat', 'zone']

# res = min(words, key=len)
# print(res)
#
# res = max(words, key=len)
# print(res)
#
# res = sorted(words, key=len)
# print(res)

# знайти слово в якому найбільше літер a

# функція яка рахує кількість a
def count_a(word):
    return word.count('a')


# res = max(words, key=count_a)
# print(res)

# інший спосід через lambda функцію
# def [назва](парам1, парам2, ..):
#     return [результат]

# lambda функція або анонімна функція
# key = lambda парам1, парам2, ..: результат

# res = max(words, key=lambda word: word.count('a'))
# print(res)
#
# key=lambda word: word.count('a')
# print(key('banana'))

# # відсортувати числа по їхнім квадратам
# nums = [1, 4, -2, 5, 6, -3]
#
# res = sorted(nums, key=lambda num: num**2)
# print(res)


# # алфавітний порядок
# "автобус" < "ананас"
# print([1, 3] < [1, 10])
#
# # відсортувати числа по їхнім квадратам, якщо вони
# # однакові тоді за самим числами
# nums = [-1, 1, 4, 2, -2, 5, 6, -3, -5]
#
# res = sorted(nums, key=lambda num: [num**2])
# print(res)
#
# res = sorted(nums, key=lambda num: [num**2, num])
# print(res)

# фільтрування
# дістати лише додатні числа зі списку
#
# nums = [-1, 1, 4, 2, -2, 5, 6, -3, -5]
#
# # filter(функція, послідовність)
# # функція має повертати True False
# func = lambda num: num > 0
# res = filter(func, nums)
#
# # перевечти результат в список
# res = list(res)
#
# print(res)

# як працює filter
def my_filter(func, items):
    new_items = []

    for item in items:
        if func(item):
            new_items.append(item)

    return new_items


# надати функції яка отримує одне число властивіть: тепер вона отримує
# список чисел і застосовується до кожного числа зі списку

def list_decorator(func):
    def new_func(nums):  # нова функція з новою властивістю
        new_nums = []

        for num in nums:
            res = func(num)  # застосовуємо оригінальну функцію
            new_nums.append(res)

        return new_nums

    return new_func


@list_decorator
def mult2(num):
    return num*2


#new_func = list_decorator(mult2)

nums = [1, 2, 3, 4, 5]
res = mult2(nums)
print(res)


