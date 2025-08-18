# Завдання 1
# Користувач вводить числа через кому. Збережіть їх у кортеж. Виведіть на екран:
# 1. Суму чисел
# 2. Найбільше та найменше число
# 3. Перші та останні 3 числа
# 4. Кількість чисел 7
# 5. Пари індекс – число
# Додатково, якщо користувач введе порожній рядок, то створіть власний кортеж з випадковими числами(12 шт).

import random

# Отримання введення
input_str = input("Введіть числа через кому (наприклад: 4, 7, 1): ")

if input_str.strip() == "":
    # Якщо рядок порожній — створюємо випадковий кортеж з 12 чисел
    numbers = tuple(random.randint(1, 100) for _ in range(12))
    print("Згенеровано випадковий кортеж:", numbers)
else:
    # Перетворення введених значень у кортеж цілих чисел
    numbers = tuple(map(int, input_str.split(',')))

# 1. Сума чисел
print("Сума чисел:", sum(numbers))

# 2. Найбільше та найменше число
print("Максимум:", max(numbers))
print("Мінімум:", min(numbers))

# 3. Перші та останні 3 числа
print("Перші 3 числа:", numbers[:3])
print("Останні 3 числа:", numbers[-3:])

# 4. Кількість чисел 7
print("Кількість сімок:", numbers.count(7))

# 5. Пари індекс – число
print("Пари індекс – число:")
for i, num in enumerate(numbers):
    print(f"{i}: {num}")


# Завдання 2
# Напишіть наступну програму: є кортеж з іменами
# зареєстрованих студентів. Користувач вводить ім’я студента
# після чого отримує повідомлення, чи студент зареєстрований.
# Програма закінчує роботу коли користувач введе порожній
# рядок

# Кортеж зареєстрованих студентів
students = ("Олег", "Ірина", "Марія", "Андрій", "Світлана")

while True:
    name = input("Введіть ім’я студента (або Enter для виходу): ").strip()

    if name == "":
        print("Завершення програми.")
        break

    if name in students:
        print(f"{name} зареєстрований(а).")
    else:
        print(f"{name} не знайдено серед зареєстрованих.")


# Завдання 3
# Напишіть наступну програму: є кортеж з назвами фільмів.
# Користувач вводить назву фільму.
#1. Якщо фільм знаходиться в першій половині кортежу,
#треба вивести ретро-фільм
#2. Якщо в другій половині – сучасний фільм
#3. Якщо один з останніх п'яти – новий фільм


# Кортеж з назвами фільмів
movies = (
    "The Shawshank Redemption",
    "Inception",
    "Pulp Fiction",
    "The Godfather",
    "Parasite",
    "The Matrix",
    "Forrest Gump",
    "Gladiator",
    "Fight Club",
    "Interstellar",
    "Schindler's List",
    "The Green Mile",
    "The Dark Knight",
    "Titanic",
    "Spirited Away",
    "La La Land",
    "Django Unchained",
    "The Grand Budapest Hotel",
    "Whiplash",
    "Everything Everywhere All At Once"
)

while True:
    title = input("Введіть назву фільму (або Enter для виходу): ").strip()

    if title == "":
        print("Завершення програми.")
        break

    if title not in movies:
        print("Фільм не знайдено.")
        continue

    index = movies.index(title)
    total = len(movies)
    half = total // 2

    if index >= total - 5:
        print("Новий фільм.")
    elif index < half:
        print("Ретро-фільм.")
    else:
        print("Сучасний фільм.")


# Завдання 4
# Напишіть функцію, яка отримує кортеж з назвами фруктів
# та слово. Потрібно повернути скільки разів дане слово
# зустрічається в кортежі (регістр неважливий). Складні назви
# теж враховуються. Приклад:
# ("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко")
# Яблуко зустрічається 3 рази

def count_fruit_in_tuple(fruits_tuple, search_word):
    """
    Підраховує, скільки разів слово зустрічається в кортежі рядків, ігноруючи регістр.
    Враховує часткові збіги.
    """
    # Лічильник для підрахунку збігів
    count = 0
    # Приводимо слово для пошуку до нижнього регістру один раз
    normalized_search = search_word.lower()

    # Ітеруємо по кожному фрукту в кортежі
    for fruit in fruits_tuple:
        if normalized_search in fruit.lower():
            count += 1

    return count


# Завдання 5
# Напишіть функцію, яка отримує кортеж з числами та
# виводить на екран статистику по кількості чисел з різною
# кількістю цифр. Приклад:
# одноцифрових – 3 шт
# двоцифрових – 5 шт
# трицифрових – 2 шт

def digit_count_stats(numbers: tuple):
    stats = {}
    for num in numbers:
        digits = len(str(abs(num)))  # враховуємо кількість цифр без знака
        stats[digits] = stats.get(digits, 0) + 1

    for digits in sorted(stats):
        if digits == 1:
            print(f"одноцифрових – {stats[digits]} шт")
        elif digits == 2:
            print(f"двоцифрових – {stats[digits]} шт")
        elif digits == 3:
            print(f"трицифрових – {stats[digits]} шт")
        else:
            print(f"{digits}-цифрових – {stats[digits]} шт")


# Завдання 6
# Користувач вводить назви товарів через кому. Потрібно
# сформувати кортеж. Також вводяться ціни товарів, які теж
# треба зберегти у кортеж. Виведіть на екран пари товар – ціна.
# Також виведіть назви найдорожчого та найдешевшого товарів.

# Введення назв товарів
products_input = input("Введіть назви товарів через кому: ")
products = tuple(item.strip() for item in products_input.split(','))

# Введення цін товарів
prices_input = input("Введіть ціни товарів через кому: ")
prices = tuple(float(item.strip()) for item in prices_input.split(','))

# Перевірка однакової довжини
if len(products) != len(prices):
    print("Кількість товарів і цін не збігається!")
else:
    # Виведення пар товар–ціна
    print("\nПари товар – ціна:")
    for name, price in zip(products, prices):
        print(f"{name} – {price} грн")

    # Пошук індексу мінімальної та максимальної ціни
    min_index = prices.index(min(prices))
    max_index = prices.index(max(prices))

    print(f"\nНайдешевший товар: {products[min_index]}")
    print(f"Найдорожчий товар: {products[max_index]}")
