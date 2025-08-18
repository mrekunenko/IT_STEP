# Завдання 1
# Є деякий текст. Виведіть по ньому статистику:
# a. кількість слів
# b. середня довжина слова
# c. найдовше слово
# d. найкоротше слово
# Додатково: якщо найдовших (найкоротших) слів декілька, то вивести усі.

text = input("Введіть текст для аналізу: ")

# Розділяємо текст на слова
words = text.split()

# a. Кількість слів
word_count = len(words)
print(f"a. Кількість слів: {word_count}")

# b. Середня довжина слова
total_length = sum(len(word) for word in words)
average_length = total_length / word_count
print(f"b. Середня довжина слова: {average_length:.2f}")

# c. Найдовше слово
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print(f"c. Найдовше слово ({max_length} символів): {', '.join(longest_words)}")

# d. Найкоротше слово
min_length = min(len(word) for word in words)
shortest_words = [word for word in words if len(word) == min_length]
print(f"d. Найкоротше слово ({min_length} символів): {', '.join(shortest_words)}")



# Завдання 2
# Є список з іменами. Видаліть лишні пробіли і переведіть
# їх у формат “Прізвище Ім’я”
# Приклад:
# Список: [
#  " іванов пЕТРО",
#  "сидорЕНКО марія ",
#  " Коваленко АНДРІЙ",
#  " мИХАЙЛЕНКО оЛЕНА "
# ]
# Результат: [
#  "Іванов Петро",
#  "Сидоренко Марія",
#  "Коваленко Андрій",
#  "Михайленко Олена"
# ]


names = [
    " іванов пЕТРО",
    "сидорЕНКО марія ",
    " Коваленко АНДРІЙ",
    " мИХАЙЛЕНКО оЛЕНА "
]

formatted_names = []
for name in names:
    # Видаляємо зайві пробіли і розділяємо на прізвище та ім'я
    surname, firstname = name.strip().split()

    # Форматуємо кожну частину (перша літера велика, решта - малі)
    formatted_surname = surname.capitalize()
    formatted_firstname = firstname.capitalize()

    # Об'єднуємо у правильному форматі
    formatted_name = f"{formatted_surname} {formatted_firstname}"
    formatted_names.append(formatted_name)

print(formatted_names)


# Завдання 3
# Є список який потенційно містить номери банківських
# карток. Для кожного елемента списку:
#  видаліть усі пробіли та дефіси
#  якщо рядок складається не з цифр або містить не 16
# символів – видаліть
#  створіть новий список куди добавте замасковані
# номери(лишаєте лише перші та останні 4 цифри а
# решту замінити на *, приклад 1234********7896
# Приклад: [
#  "1234 5678 9012 3456",
#  " 4444-3333-2222-1111",
#  "abcd efgh ijkl mnop",
#  "000011112222333",
#  "9999-8888-7777-6666",
#  "1111 2222 3333 4444 extra",
#  "5555-6666-7777-8888"
# ]
# Результат: [
# '1234********3456',
# '4444********1111',
# '9999********6666',
# '5555********8888'
# ]

cards = [
    "1234 5678 9012 3456",
    " 4444-3333-2222-1111",
    "abcd efgh ijkl mnop",
    "000011112222333",
    "9999-8888-7777-6666",
    "1111 2222 3333 4444 extra",
    "5555-6666-7777-8888"
]

valid_cards = []

for card in cards:
    # Видаляємо всі пробіли та дефіси
    cleaned = card.replace(" ", "").replace("-", "")

    # Перевіряємо чи рядок складається лише з цифр і має 16 символів
    if cleaned.isdigit() and len(cleaned) == 16:
        # Маскуємо номер (перші 4 та останні 4 цифри, решта - *)
        masked = cleaned[:4] + "*" * 8 + cleaned[-4:]
        valid_cards.append(masked)

print(valid_cards)