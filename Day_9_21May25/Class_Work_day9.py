# while True:
#     num = int(input('число '))
#
#     if num < 0:
#         print("Число не може біти від'ємним")
#         continue
#
#     if num == 0:
#         break
#
#     print("Ви ввел число правильно, програма працює надалі")
#
#     print(2*num)
#
#
# print("цикл закінчився")
# print("Кінець програми")






# Напишіть програму для виведення таблиці співвідношення
# температур, виражених у градусах Цельсія, Фаренгейта та
# Кельвіна. У таблиці повинні розміщуватись всі температури
# між 0 та 100 градусами Цельсія, кратні 10.
# Доповніть таблицю відповідними заголовками.

# print("цельції    фаренгейти    Келвін")
#
# for celcius in range(0, 101, 10):
#     far = celcius * 1.8 + 32
#     kelvin = 273.15 + celcius
#
#     print(f"{celcius:^3}         {far:^5}        {kelvin}")


# for num in range(10):
#     print(num)
#
# for num in range(10, 20):
#     print(num)

# for num in range(10, 20, 2):
#     print(num)

# for num in range(20, 10, -1):
#     print(num)





# Початковий внесок в банку дорівнює 1000 грн.
# Через кожен місяць розмір вкладу збільшується
# на P відсотків від наявної суми (P - дійсне число, 0 <P <25).
# За даним P визначити, через скільки місяців розмір вкладу
# перевищить 1100 грн., і вивести знайдену кількість місяців
# і підсумковий розмір вкладу S

# користувач вводить відсоток
# while True:
#     percent = int(input("Введіть відсоток від 0 до 25: "))
#
#     # if percent > 0 and percent < 25:
#     #     break
#
#     if 0 < percent < 25:
#         break


# рахуємо суму депозиту
balance = 1000
target_balance = 1100
month_count = 0

# while True:
#     month_count += 1
#     balance += percent / 100 * balance
#
#     if balance > target_balance:
#         break


# # теж саме через цикл for
#
# for month_count in range(1, 100000000000000000):
#     balance += percent / 100 * balance
#
#     if balance > target_balance:
#         break
#
# print(f"місяці {month_count}")
# print(f"баланс {balance}")



# Написати програму для конвертації валют.
# Користувачу пропонується меню
# 1. долари
# 2. євро
# 3. єни
# 4. вихід
# Після чого користувач вводить суму в гривнях,
# а програма переводить їх в обрану валюту

usd_rate = 41.4851
euro_rate = 46.6521
jpy_rate = 0.2849


while True:
    # меню
    print("Оберіть одну з команд")
    print("1. долари")
    print("2. євро")
    print("3. єни")
    print("4. вихід")

    # користувач робить вибір
    choice = int(input("Введіть номер команди: "))

    # чи закінчувати програму
    if choice == 4:
        print("Кінець програми")
        break

    # користувач вводить додаткові дані
    uah = float(input("Введіть суму в гривнях: "))

    # перевірка чи правильні дані
    if uah < 0:
        print("Сума має бути додатньою")
        continue

    # обробка вибору користувача
    if choice == 1:
        usd = uah / usd_rate
        print(f"{uah} гривень = {usd:.2f} доларів")

    elif choice == 2:
        euro = uah / euro_rate
        print(f"{uah} гривень = {euro:.2f} євро")

    elif choice == 3:
        jpy = uah / jpy_rate
        print(f"{uah} гривень = {jpy:.2f} єн")

    else:
        print("error")
        print("Невідома команда")