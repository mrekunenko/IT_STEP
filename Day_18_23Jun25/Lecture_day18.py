# документація

# def get_greeting(name, age=10, verbose=False):
#     """
#     Створює привітання та повертає як результат.
#     Якщо verbose=True то виводить привітання на екран
#
#     Параметри:
#         name: str
#             ім'я користувача
#
#         age: int
#             вік користувача, має бути додатнім, default 10
#
#         verbose: bool
#             чи виводити повідомлення на екран, default False
#
#     Return:
#         str -- текст привітання
#     """
#
#     if age < 0:
#         print("Вік має бути додатнім")
#         return
#
#     text = f"Привіт, {name}, тобі {age} років"
#
#     if verbose:
#         print(text)
#
#     return text
# #
# #
# # help(get_greeting)
#
#
# # використання функцій
#
# def greet_users(users, verbose=False):
#     """
#     Виводить привітання кожному користувачу
#
#     Параметри:
#         users: list[str]
#             список з іменами користувачів
#
#         verbose: bool
#             чи виводити повідомлення на екран,
#             див get_greeting
#     """
#
#     greetings = []
#
#     for user in users:
#         greeting = get_greeting(user, verbose=verbose)
#         greetings.append(greeting)
#         print(greeting)

#
# line1 = [1, 2, 3]
# line2 = [4, 5, 6]
#
# # таблиця з двох рядків та трьох стовпчиків
# table = [line1,
#          line2]
#
# # те саме в один рядок
# table = [[1, 2, 3],
#          [4, 5, 6]]
#
#
# print(table[0])  # перший рядок
# print(table[-1])  # останній рядок
#
# # table[індекс рядка][індекс стовпчика]
# print(table[0][2])  # елемент 3
#
# # перший стовпчик
# column = []
# for line in table:
#     item = line[2]
#     column.append(item)
#
# print(column)
#
# print(table)