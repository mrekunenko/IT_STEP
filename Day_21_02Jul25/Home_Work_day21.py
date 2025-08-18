# Завдання 1
# Є кортеж з назвами міст. Виведіть ті міста, які
# зустрічаються в кортежі більше одного разу.

def find_duplicates(cities: tuple):
    seen = set()
    duplicates = set()

    for city in cities:
        if city in seen:
            duplicates.add(city)
        else:
            seen.add(city)

    if duplicates:
        print("Міста, які повторюються:", ', '.join(duplicates))
    else:
        print("Повторюваних міст немає.")


cities = ("Київ", "Львів", "Одеса", "Київ", "Харків", "Львів", "Дніпро")
find_duplicates(cities)


# Завдання 2
# Є два кортежі з випадковими числами. Виведіть на екран
# ті числа, які є в першому кортежі, але немає в другому.

def unique_from_first(tuple1: tuple, tuple2: tuple):
    result = tuple(set(tuple1) - set(tuple2))
    if result:
        print("Числа, які є в першому кортежі, але немає в другому:", result)
    else:
        print("Усі числа з першого кортежу є і в другому.")


a = (1, 3, 5, 7, 9, 11)
b = (3, 6, 9, 12)
unique_from_first(a, b)


# Завдання 3
# Напишіть функцію, яка отримує 2 кортежі. Поверніть
# список з елементами, які є в обох кортежах і мають однакові
# індекси. Підказка: використайте zip()

def common_elements_by_index(t1: tuple, t2: tuple) -> list:
    return [a for a, b in zip(t1, t2) if a == b]

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (1, 9, 3, 0, 5, 7)
result = common_elements_by_index(tuple1, tuple2)
print("Спільні елементи з однаковими індексами:", result)

