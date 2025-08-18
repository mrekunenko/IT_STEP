# Завдання 1
# Користувач вводить імена людей, поки не введе порожній
# рядок. Збережіть усі імена в множині. Якщо ім’я вводиться
# повторно, то вивести повідомлення про це.
# Виведіть кількість людей


def collect_names():
    """
    Збирає імена від користувача, поки не буде введено порожній рядок.
    Повертає множину унікальних імен.
    """
    names = set()

    print("Введіть імена людей (Enter для завершення):")
    while True:
        name = input("Ім'я: ").strip()

        if not name:  # Порожній рядок - завершення введення
            break

        if name in names:
            print(f"Ім'я '{name}' вже було додано раніше!")
        else:
            names.add(name)

    return names


def main():
    """Головна функція програми"""
    unique_names = collect_names()

    print("\nРезультат:")
    print(f"Кількість унікальних імен: {len(unique_names)}")
    print("Список імен:", ", ".join(unique_names) if unique_names else "немає імен")


if __name__ == "__main__":
    main()


# Завдання 2
# Студентів розбили на 2 групи, кожна з яких навчається у
# свій день. Перевірте чи не виникло помилки, а саме
# 1. Чи немає студентів які є в двох групах одночасно (якщо
# є, то вивести їх імена)
# 2. Чи немає студентів, про яких забули (якщо є, то вивести
# імена)
# Напишіть відповідну функцію, яка отримує два списки з
# іменами студентів кожної групи, та список усіх студентів.
# Додатково: змініть код, якщо груп 3


def check_student_groups(group1, group2, all_students):
    """
    Перевіряє розподіл студентів на групи на наявність помилок.

    Параметри:
    - group1: список студентів першої групи
    - group2: список студентів другої групи
    - all_students: список усіх студентів

    Повертає словник з результатами перевірки.
    """
    # Перетворюємо списки у множини для зручності операцій
    set_group1 = set(group1)
    set_group2 = set(group2)
    set_all = set(all_students)

    # 1. Знаходимо студентів, які є в обох групах
    common_students = set_group1 & set_group2

    # 2. Знаходимо студентів, яких забули включити до груп
    forgotten_students = set_all - (set_group1 | set_group2)

    return {
        'common_students': list(common_students),
        'forgotten_students': list(forgotten_students)
    }


# Функція для 3 груп
def check_student_groups_3(group1, group2, group3, all_students):
    """
    Перевіряє розподіл студентів на 3 групи на наявність помилок.

    Параметри:
    - group1: список студентів першої групи
    - group2: список студентів другої групи
    - group3: список студентів третьої групи
    - all_students: список усіх студентів

    Повертає словник з результатами перевірки.
    """
    set_group1 = set(group1)
    set_group2 = set(group2)
    set_group3 = set(group3)
    set_all = set(all_students)

    # 1. Знаходимо студентів, які є в декількох групах
    common_in_1_2 = set_group1 & set_group2
    common_in_1_3 = set_group1 & set_group3
    common_in_2_3 = set_group2 & set_group3
    common_in_all = set_group1 & set_group2 & set_group3

    all_common = common_in_1_2 | common_in_1_3 | common_in_2_3 | common_in_all

    # 2. Знаходимо студентів, яких забули включити до груп
    forgotten_students = set_all - (set_group1 | set_group2 | set_group3)

    return {
        'common_students': list(all_common),
        'forgotten_students': list(forgotten_students)
    }


# Приклад використання для 2 груп
if __name__ == "__main__":
    # Приклад даних
    all_students = ["Олег", "Марія", "Іван", "Софія", "Андрій", "Катерина"]
    group1 = ["Олег", "Марія", "Іван"]  # Перша група
    group2 = ["Іван", "Софія", "Андрій"]  # Друга група

    # Виклик функції
    result = check_student_groups(group1, group2, all_students)

    # Вивід результатів
    print("Результати перевірки для 2 груп:")
    if result['common_students']:
        print("Студенти, які є в обох групах:", ", ".join(result['common_students']))
    else:
        print("Немає студентів, які є в обох групах")

    if result['forgotten_students']:
        print("Студенти, яких забули включити до груп:", ", ".join(result['forgotten_students']))
    else:
        print("Всі студенти включені до груп")

# Приклад використання для 3 груп
if __name__ == "__main__":
    # Приклад даних
    all_students = ["Олег", "Марія", "Іван", "Софія", "Андрій", "Катерина", "Наталія"]
    group1 = ["Олег", "Марія", "Іван"]
    group2 = ["Іван", "Софія", "Андрій"]
    group3 = ["Андрій", "Катерина", "Марія"]

    # Виклик функції
    result = check_student_groups_3(group1, group2, group3, all_students)

    # Вивід результатів
    print("\nРезультати перевірки для 3 груп:")
    if result['common_students']:
        print("Студенти, які є в декількох групах:", ", ".join(result['common_students']))
    else:
        print("Немає студентів, які є в декількох групах")

    if result['forgotten_students']:
        print("Студенти, яких забули включити до груп:", ", ".join(result['forgotten_students']))
    else:
        print("Всі студенти включені до груп")


# Завдання 3
# Є словник з цінами продуктів, де ключ – назва продукту, а
# значення – ціна за кг. Організуйте просту роботу магазину:
# користувач вводить назву продукту та вагу, потрібно вивести
# загальну ціну.

# Словник з продуктами та їх цінами
products = {
    "Яблука": 25.50,
    "Банани": 35.75,
    "Апельсини": 40.20,
    "Мандарини": 45.90,
    "Виноград": 60.00
}

# Головна програма
total = 0.0

print("Доступні продукти:")
for product, price in products.items():
    print(f"- {product}: {price} грн/кг")

while True:
    print("\nВведіть назву продукту (або 'вихід' для завершення):")
    product = input().strip().capitalize()

    if product == "Вихід":
        break

    if product not in products:
        print("Помилка: такого продукту немає в наявності")
        continue

    print(f"Введіть вагу для {product} (кг):")
    weight_input = input().strip()

    # Перевірка чи вага є числом
    is_valid = True
    for char in weight_input:
        if not (char.isdigit() or char == '.'):
            is_valid = False
            break

    if not is_valid or weight_input.count('.') > 1:
        print("Помилка: некоректний формат ваги")
        continue

    weight = float(weight_input)
    if weight <= 0:
        print("Помилка: вага повинна бути більше 0")
        continue

    cost = products[product] * weight
    total += cost
    print(f"Вартість {weight} кг {product}: {cost:.2f} грн")

print(f"\nЗагальна сума до сплати: {total:.2f} грн")


# Завдання 4
# Є словник з інформацією про вміст вітаміну С в різних
# продуктах, де ключ – назва продукту, значення – вміст
# вітаміну С у мг. Користувач вводить свій раціон: список з
# назвами продуктів
# Обчисліть вміст вітаміну С в раціоні(якщо у словнику
# немає якогось продукту, вважайте вміст вітаміну рівним 0 мг).
# Виведіть продукт з найбільшим вмістом вітаміну С.

# Словник з вмістом вітаміну С (мг на 100г продукту)
vitamin_c_content = {
    "Шипшина": 650,
    "Чорна смородина": 200,
    "Петрушка": 150,
    "Болгарський перець": 120,
    "Ківі": 90,
    "Брокколі": 89,
    "Цитрусові": 50,
    "Капуста": 45,
    "Помідори": 25,
    "Яблука": 10
}

# Отримання раціону від користувача
print("Введіть свій раціон (продукти через кому):")
diet_input = input().strip()

# Обробка введених даних
diet = [product.strip().capitalize() for product in diet_input.split(',')]

# Розрахунок вмісту вітаміну С
total_vitamin_c = 0
max_vitamin_product = None
max_vitamin_amount = 0

for product in diet:
    amount = vitamin_c_content.get(product, 0)
    total_vitamin_c += amount

    if amount > max_vitamin_amount:
        max_vitamin_amount = amount
        max_vitamin_product = product

# Виведення результатів
print(f"\nЗагальний вміст вітаміну С: {total_vitamin_c} мг")

if max_vitamin_product:
    print(f"Продукт з найбільшим вмістом вітаміну С: {max_vitamin_product} ({max_vitamin_amount} мг)")
else:
    print("У вашому раціоні немає продуктів з відомим вмістом вітаміну С")


# Завдання 5
# Склад футбольної команди розподіляється між такими
# позиціями:
# 1) воротар – 1
# 2) захисник – 4
# 3) півзахисник – 4
# 4) нападник – 2
# Користувач поступово вводить імена гравців та їх позиції.
# Потрібно зберегти ці дані у словник, де ключ – назва позиції,
# значення – список з іменами гравців на цю позицію. Перевірте
# чи склад команди правильний.
# Також виведіть імена всіх гравців.

def input_players():
    """
    Функція для введення гравців та їх позицій.
    Повертає словник зібраних даних.
    """
    team = {
        'воротар': [],
        'захисник': [],
        'півзахисник': [],
        'нападник': []
    }

    print("Введіть імена гравців та їх позиції (або 'стоп' для завершення):")
    print("Доступні позиції: воротар, захисник, півзахисник, нападник")

    while True:
        name = input("Ім'я гравця: ").strip()
        if name.lower() == 'стоп':
            break

        position = input("Позиція: ").strip().lower()

        if position not in team:
            print("Невірна позиція! Спробуйте ще раз.")
            continue

        team[position].append(name)

    return team


def validate_team(team):
    """
    Перевіряє чи склад команди відповідає вимогам.
    Повертає True якщо склад вірний, False - якщо ні.
    """
    requirements = {
        'воротар': 1,
        'захисник': 4,
        'півзахисник': 4,
        'нападник': 2
    }

    for position, count in requirements.items():
        if len(team[position]) != count:
            print(f"Помилка: на позиції '{position}' має бути {count} гравці(в), а є {len(team[position])}")
            return False

    return True


def print_all_players(team):
    """Виводить список усіх гравців команди."""
    print("\nСписок усіх гравців команди:")
    for position, players in team.items():
        print(f"{position.capitalize()}: {', '.join(players)}")


# Основна програма
if __name__ == "__main__":
    team = input_players()

    if validate_team(team):
        print("\nСклад команди вірний!")
    else:
        print("\nУвага! Склад команди не відповідає вимогам.")

    print_all_players(team)


# Завдання 6
# Організуйте фільтр товарів в онлайн магазині. Усі товари
# діляться на певні категорії, причому один і той самий товар
# може відноситись до різних категорій. Є словник, де ключі –
# назви категорій, а значення – множини з товарами цієї
# категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які
# відносяться одночасно до цих двох категорій.
# Додатково: змініть код якщо користувач вводить декілька
# категорій.


def filter_products(categories):
    """
    Функція для фільтрації товарів за категоріями.
    categories - словник категорій та товарів.
    """
    print("Доступні категорії:", ", ".join(categories.keys()))

    # Отримуємо категорії від користувача
    input_categories = input("Введіть категорії через кому: ").strip().split(',')
    selected_categories = [cat.strip() for cat in input_categories if cat.strip() in categories]

    if not selected_categories:
        print("Не обрано жодної валідної категорії")
        return

    # Знаходимо спільні товари
    common_products = None
    for cat in selected_categories:
        if common_products is None:
            common_products = categories[cat].copy()
        else:
            common_products &= categories[cat]

    # Виводимо результати
    if common_products:
        print("\nСпільні товари для категорій:", ", ".join(selected_categories))
        for product in sorted(common_products):
            print(f"- {product}")
    else:
        print("\nНемає спільних товарів для обраних категорій")


# Приклад використання
if __name__ == "__main__":
    # Приклад бази даних товарів
    products_db = {
        "Електроніка": {"Смартфон", "Ноутбук", "Планшет", "Навушники"},
        "Побутова техніка": {"Холодильник", "Пральна машина", "Планшет", "Смартфон"},
        "Офіс": {"Принтер", "Ноутбук", "Сканнер", "Планшет"},
        "Розваги": {"Навушники", "Смартфон", "Планшет", "Телевізор"}
    }

    filter_products(products_db)