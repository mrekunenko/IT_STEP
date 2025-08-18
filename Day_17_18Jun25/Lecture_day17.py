# перевірка типів даних

# def get_sum(num1, num2):
#     # перевірка що num1 типу int або float
#     if not isinstance(num1, (int, float)):
#         print('Неправильний тип даних')
#         return
#
#     if not isinstance(num2, (int, float)):
#         print('Неправильний тип даних')
#         return
#
#     result = num1 + num2
#
#     return result
#
#
# print(get_sum(2.5, 3))
# print(get_sum('text1', '  text2'))
# print(get_sum(2, '3'))

# декілька значень в return

def statistics(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    mean = (num1 + num2) / 2

    return min_num, max_num, mean


# result = statistics(2, 3)
# print(result)
# print(type(result))
#
# print(result[0])
# print(result[-1])

# min_num, max_num, mean = statistics(2, 5)
#
# print(max_num)

# text1, text2, text3 = 'dog'
# a, b, c = 1, 2, 10
#
# print(b)

# # якщо потрібно не все
# # _ -- змінна для зберігання непотребу
#
# _, _, mean = statistics(2, 5)
# _, max_, _ = statistics(2, 5)
# min_, _, mean = statistics(2, 5)
#
# _, _, _ = statistics(2, 5)
# statistics(2, 5)
#
# #res = 2 + 3*10
# print(_)
#
# # for _ in range(10):
# #     print('hello')

# параметри за замовчування

# def get_sum(num1=10, num2=10):
#     print(f"{num2 = }")
#     return num1 + num2
#
#
# print(get_sum(2, 3))
# print(get_sum(2))
# print(get_sum())

# функція перевіряє чи є текст реченням, тобто
# закінчується на певний символ(за замовчуванням .)

# def is_sentence(text, symbol='.'):
#     # text -- позиційний
#     # symbol -- іменний
#
#     # позиційні параметри МАЮТЬ йти першими
#
#     return text + symbol
#
# user_text = 'hello.'
#
# print(is_sentence(user_text, symbol='?'))
# print(is_sentence(user_text, '?'))
# print(is_sentence(text=user_text, symbol='?'))
# print(is_sentence(symbol='?', text=user_text))
# # print(is_sentence(symbol='?', user_text))  # Помилка
#
# print(is_sentence(user_text))
# print(is_sentence(text=user_text))


# def func(num, nums=[]):
#     nums.append(num)
#
#     print(nums)
#     return len(nums)
#
# func(1)
# func(2)
# func(3)

# def func(num, nums=None):
#     if nums is None:
#         nums = []
#
#     nums.append(num)
#
#     print(nums)
#     return len(nums)
#
# func(1)
# func(2)
# func(3)



# # Функція рахує добуток чисел з списку та, якщо вказати,
# # виводить інформацію про свою роботу

# def product(nums, verbose=False):
#     # перевірка типів даних
#     if not isinstance(nums, list):
#         print("Ви маєте передати список чисел")
#         return
#
#     if not isinstance(verbose, bool):
#         print("verbose має бути типу bool")
#         return
#
#     res = 1
#
#     for num in nums:
#         # елементи списку числа
#         if not isinstance(num, (int, float)):
#             print("елементи списку мають бути числами")
#             return
#
#         res *= num
#
#     # чи треба виводити результат
#     if verbose:
#         print(f"Добуток чисел рівний -- {res}")
#
#     return res
#
# #print(product([1, 2, 3, 4]))
# #print(product([1, 2, '3', 4]))
# print(product([1, 2, 3, 4], True))
# print(product([1, 2, 3, 4], verbose=True))
# print(product([1, 2, 3, 4], verbose=False))
# print(product([1, 2, 3, 4], verbose='true'))
# print(product('123', verbose='true'))
# print(product(verbose=True, nums=[1, 2, 3, 4]))



# # Функція отримує ціну товару, податок(за замовчуванням 0.20)
# # та знижку(за замовчуванням 0). Поверніть кінцеву ціну


def get_price(price, tax=0.2, discount=0, is_percentage=False):
    # перевірки
    if not isinstance(price, (int, float)) or price < 0:
        print("Ціна має бути дадатнім числом")
        return

    if not isinstance(tax, (int, float)) or not (0 <= tax <= 100):
        print("Податок має бути числом в діапазоні [0, 100]")
        return

    if not isinstance(discount, (int, float)) or not (0 <= discount <= 100):
        print("Знижка має бути числом в діапазоні [0, 100]")
        return

    # робота з відсотками
    if is_percentage:
        tax /= 100
        discount /= 100

    # основна програма

    price *= (1 + tax)  # нарахування податку
    price *= (1 - discount)  # знижка

    return price


# print(get_price(100))
# print(get_price(100, 0.5))
# print(get_price(100, 0.5, 0.2))
print(get_price(100, tax=0.5, discount=0.2))
print(get_price(100, discount=0.2, tax=0.5))
print(get_price(100, discount=20, tax=50, is_percentage=True))
print(get_price(-100, discount=0.2, tax=0.5))
