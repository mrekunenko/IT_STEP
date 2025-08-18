# винятки

# # іноді зробити перевірку через if буває дуже складно
# str_num = input("Введіть число ")
#
# if str_num.isdigit():  # не враховує -123, +5, 456.7894
#     num = int(str_num)
#     print(num)
# else:
#     print("Введено не число")


# try:
#     # тут може виникнути помилка(виняток)
#     num = float(input("Введіть число "))
#     print(num)
# except ValueError:
#     print('ви ввели не число')
#     num = 0
#
# except ZeroDivisionError:
#     print('ділення на 0')
#     num = 0
#
# except Exception:  # обробка будь-якого винятку
#     print('помилка')
#     num = 0
#
#
# print('Кінець програми')
#
# if num > 0:
#     print("positive")
# else:
#     print('negative')

# if case == 1:
#     pass
# elif case == 2:
#     pass
# elif case == 3:
#     pass

# функція яка просить у користувача число
# def get_age():
#     while True:
#         try:
#             age = int(input('Введіть вік: '))
#         except Exception:
#             print('Ввели не число')
#             continue
#
#         if age < 0:
#             print('вік не може бути від\'ємним')
#             continue
#
#         return age
#
#
# age = get_age()
# print(age)


# Напишіть функцію, яка приймає список чисел і
# повертає їхнє середнє арифметичне.
# Обробіть можливий виняток, коли список порожній.


# def average(nums):
#     try:
#         total = sum(nums)
#         count = len(nums)
#         return total / count
#     except TypeError:
#         print("Помилка: не всі елементи є числами")
#         return None
#     except ZeroDivisionError:
#         print("Помилка: список порожній")
#         return None
#
#
# nums = [1, 23]
# res = average(nums)
# print(res)





# винятки у функціях

# def get_name():
#     name = input('Введіть ім\'я: ')
#
#     if name == '':
#         raise ValueError('ім\'я не може бути порожнім')
#
#     if not name.isalpha():
#         raise ValueError(f'ім\'я має містити лише літери: {name}')
#
#     return name
#
#
# try:
#     name = get_name()
#     print(name)
# except Exception as err:  # err = помилка
#     print(f'Помилка: {err}')






# Напишіть функцію, яка приймає список і елемент,
# який слід видалити зі списку. Обробіть можливий виняток,
# коли такого елементу немає у списку.


def delete(items, item):
    try:
        items.remove(item)
        print(f"Елемент {item} успішно видалено")
    except ValueError:
        print(f'Такого елементу немає в списку {item}')
    except AttributeError:
        print(f"Ви передали не послідовність або послідовність незмінна")
    except Exception as err:
        print(f"Помилка: {err}")


delete([1, 2, 3], 'hello')
delete(12, 1)