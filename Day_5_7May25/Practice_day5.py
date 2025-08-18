# # Завдання 2
# # Оформіть чек покупки. Користувач вводить ціну за
# # одиницю товару, кількість товару та свій вік.
# # Якщо користувач неповнолітній або старший за 65 років,
# # то застосуйте знижку 15%
#
# # Введення даних від користувача
# tsina_za_odynytsyu = float(input("Введіть ціну за одиницю товару: "))
# kilkist_tovaru = int(input("Введіть кількість товару: "))
# vik_korystuvacha = int(input("Введіть свій вік: "))
#
# # Обчислення загальної суми
# zagalna_tsina = tsina_za_odynytsyu * kilkist_tovaru
#
# # Перевірка на знижку
# if vik_korystuvacha < 18 or vik_korystuvacha > 65:
#     znyzhka = 0.15
#     suma_z_znyszkoyu = zagalna_tsina * (1 - znyzhka)
# else:
#     znyzhka = 0.0
#     suma_z_znyszkoyu = zagalna_tsina
#
# # Виведення чека
# print("Чек покупки")
# print(f"Ціна за одиницю: {tsina_za_odynytsyu} грн")
# print(f"Кількість товару: {kilkist_tovaru}")
# print(f"Загальна сума: {zagalna_tsina:.2f} грн")
#
# if znyzhka > 0:
#     print(f"Знижка: {int(znyzhka * 100)}%")
#     print(f"Сума зі знижкою: {suma_z_znyszkoyu:.2f} грн")
# else:
#     print("Знижка: не надається")


# Завдання 4
# Користувач вводить ціле число.
# - Якщо воно ділиться на 3, виведіть Fizz
# - Якщо воно ділиться на 5, виведіть Buzz
# - Якщо ділиться на 3 і 5, виведіть FizzBuzz

# Введення цілого числа від користувача
vvedene_chyslo = int(input("Введіть ціле число: "))

# Логічна перевірка з умовами
if vvedene_chyslo % 3 == 0 and vvedene_chyslo % 5 == 0:
    print("FizzBuzz")
elif vvedene_chyslo % 3 == 0:
    print("Fizz")
elif vvedene_chyslo % 5 == 0:
    print("Buzz")
else:
    print("Число не ділиться на 3 або 5")


# Завдання 6
# Користувач вводить 3 довжини: a, b, c. Виведіть «Так» або # «Ні»
# в залежності чи можна побудувати з цими сторонами трикутник.
# Трикутник можна побудувати якщо:
# 1. Усі сторони додатні
# 2. Сума будь-яких двох сторін більша за третю
# (треба перевірити усі можливі комбінації)

# Отримання довжин сторін від користувача
a = float(input("Введіть довжину сторони a: "))
b = float(input("Введіть довжину сторони b: "))
c = float(input("Введіть довжину сторони c: "))

# Перевірка умов існування трикутника
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("Так")
else:
    print("Ні")

