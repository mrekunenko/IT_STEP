# Завдання 1
# Напишіть функцію, яка отримує 2 словника та об’єднує їх в один.
# Якщо ключі співпадають то потрібно додати відповідні їм значення.

def merge_dicts(dict1, dict2):
    """
    Об'єднує два словника.
    Якщо ключі співпадають — додає значення.
    """
    result = dict1.copy()  # копіюємо перший словник

    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result


# Завдання 2
# Напишіть функцію, яка отримує словник та інвертує його,
# тобто повертає новий словник, де ключі та значення змінені
# місцями.

def simple_invert(original_dict: dict) -> dict:

  return {value: key for key, value in original_dict.items()}


student_ids = {'alice': 101, 'bob': 102, 'charlie': 103}
id_students = simple_invert(student_ids)

print(f"Вихідний словник: {student_ids}")
print(f"Інвертований словник: {id_students}")


# Завдання 3
# Користувач вводить назви товарів та їх ціни поки не введе
# порожній рядок. Збережіть дані у словник. Якщо користувач
# вводить товар повторно та треба додати стару та нову ціни.
# В кінці виведіть таблицею товар – ціна. Також виведіть
# загальну ціну.

def collect_products():
    products = {}

    while True:
        name = input("Введіть назву товару (або ENTER для завершення): ").strip()
        if name == "":
            break

        price_input = input(f"Введіть ціну для '{name}': ").strip()
        if price_input.replace('.', '', 1).isdigit():  # дозволяє десяткові числа
            price = float(price_input)
        else:
            print("Ціна має бути числом. Спробуйте ще раз.")
            continue

        if name in products:
            products[name] += price
        else:
            products[name] = price

    return products


def print_table(products):
    print("\nТовар\t\tЦіна")
    print("-" * 25)
    total = 0
    for name, price in products.items():
        print(f"{name}\t\t{price}")
        total += price
    print("-" * 25)
    print(f"Загальна сума:\t{total}")


# Завдання 4
# Напишіть функцію, яка отримує текст та повертає
# словник, де ключі – це слова, а значення – їхня кількість в
# тексті.
# Добавте параметр за замовчуванням який визначає, чи
# значення в словнику будуть кількостями слів, чи
# частотою(відсотком від загальної кількості).


def count_words(text, frequency=False):

    words = text.lower().split()
    total = len(words)
    word_counts = {}

    for word in words:
        word = word.strip('.,!?:;"\'()[]')  # очищення від розділових знаків
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1

    if frequency:
        for word in word_counts:
            word_counts[word] = round((word_counts[word] / total) * 100, 2)

    return word_counts


text = input("Введіть текст: ")

# Підрахунок кількостей
counts = count_words(text)
print("\nКількість слів:")
print(counts)

# Підрахунок частот
freq = count_words(text, frequency=True)
print("\nЧастота слів (%):")
print(freq)


# Завдання 5
# Створіть словник, де ключі – це назви груп, а значення –
# списки студентів, що належать до цих груп.
# Реалізуйте 3 функції для додавання та видалення студентів
# з груп, а також для виведення даних на екран.

# Словник з групами студентів
groups = {}


def add_student(group_name, student_name):
    """
    Додає студента до групи. Якщо групи немає - створює її.
    """
    # Перевіряємо чи існує група
    if group_name not in groups:
        groups[group_name] = []  # Створюємо нову групу

    # Перевіряємо чи студент вже є в групі
    if student_name not in groups[group_name]:
        groups[group_name].append(student_name)
        print(f"Студент '{student_name}' додано до групи '{group_name}'")
    else:
        print(f"Студент '{student_name}' вже є в групі '{group_name}'")


def remove_student(group_name, student_name):
    """
    Видаляє студента з групи.
    """
    # Перевіряємо чи існує група
    if group_name not in groups:
        print(f"Група '{group_name}' не існує")
        return

    # Перевіряємо чи студент є в групі
    if student_name in groups[group_name]:
        groups[group_name].remove(student_name)
        print(f"Студент '{student_name}' видалено з групи '{group_name}'")

        # Якщо група стала порожньою, видаляємо її
        if len(groups[group_name]) == 0:
            groups.pop(group_name)
            print(f"Група '{group_name}' була видалена (порожня)")
    else:
        print(f"Студент '{student_name}' не знайдено в групі '{group_name}'")


def show_groups():
    """
    Виводить всі групи та студентів на екран.
    """
    if not groups:
        print("Немає жодної групи")
        return

    print("=== СПИСОК ГРУП ===")
    for group_name, students in groups.items():
        print(f"\nГрупа '{group_name}' ({len(students)} студентів):")
        if students:
            for i, student in enumerate(students, 1):
                print(f"  {i}. {student}")
        else:
            print("  (порожня)")


# Завдання 6
# Напишіть функцію, яка запитує в користувача ім’я, вік,
# посаду та повертає ці дані у вигляді словника.
# Створіть іншу функцію, яка добавляє 5 людей у словник,
# де ключ ім’я, а значення – словник з попередньої функції.
# Після чого виведіть середній вік.

def get_employee_info():
    """Запитує дані про працівника та повертає словник"""
    name = input("Введіть ім'я працівника: ")
    age = int(input("Введіть вік працівника: "))
    position = input("Введіть посаду працівника: ")

    return {
        'name': name,
        'age': age,
        'position': position
    }


def create_employees_dict():
    """Створює словник з 5 працівниками"""
    employees = {}

    print("Введіть дані 5 працівників:")
    for i in range(5):
        print(f"\nПрацівник #{i + 1}")
        employee_info = get_employee_info()
        employees[employee_info['name']] = {
            'age': employee_info['age'],
            'position': employee_info['position']
        }

    return employees


def calculate_average_age(employees):
    """Розраховує середній вік працівників"""
    total_age = 0
    count = 0

    for employee in employees.values():
        total_age += employee['age']
        count += 1

    return total_age / count if count > 0 else 0


# Основна програма
if __name__ == "__main__":
    employees_dict = create_employees_dict()

    print("\nСписок працівників:")
    for name, info in employees_dict.items():
        print(f"{name}: Вік - {info['age']}, Посада - {info['position']}")

    average_age = calculate_average_age(employees_dict)
    print(f"\nСередній вік працівників: {average_age:.1f} років")