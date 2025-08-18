# Завдання 1
# Є текстовий файл. Запишіть в інший файл таку
# статистику:
#  Кількість символів
#  Кількість рядків
#  Кількість цифр
#  Кількість голосних літер(aeuio)

# text_file = r"D:\PyCharm\IT_STEP\Day_26_11Aug25\text_file.txt"
# output_file = r"D:\PyCharm\IT_STEP\Day_26_11Aug25\text_file2.txt"

with open(r"D:\PyCharm\IT_STEP\Day_26_11Aug25\text_file.txt", 'r', encoding='UTF-8') as file:
    text = file.read()

char_count = len(text.replace('\n', ''))
line_count = len(text.splitlines())
digit_count = sum(1 for char in text if char.isdigit())
vowel_count = sum(1 for char in text.lower() if char in 'aeuio')

with open(r"D:\PyCharm\IT_STEP\Day_26_11Aug25\text_file2.txt", 'w', encoding='UTF-8') as file:
    file.write(f'Кількість символів: {char_count}\n')
    file.write(f'Кількість рядків: {line_count}\n')
    file.write(f'Кількість цифр: {digit_count}\n')
    file.write(f'Кількість голосних літер (aeuio): {vowel_count}')

print(f'Статистика збережена у файл {r"D:\PyCharm\IT_STEP\Day_26_11Aug25\text_file2.txt"}')


# Завдання 2
# Користувач вводить слово та назву файлу. Виведіть
# кількість цього слова у файлі.

search_word= input("Введіть слово для пошуку: ")
filename = input("Введіть назву файлу: ")

with open(filename, 'r', encoding='UTF-8') as file:
    text = file.read()

words = text.split()
word_count = 0

for word in words:
    clean_word = word.strip('.,!?;:"()[]{}')
    if clean_word.lower() == search_word.lower():
        word_count =+ 1

print(f"Кількість слова '{search_word}': {word_count}")


# Завдання 3
# Є текстовий файл. Видаліть з нього останній рядок.

filename = input("Введіть назву файлу: ")

with open(filename, 'r', encoding='UTF-8') as file:
    lines = file.readlines()


if lines:
    # Видаляємо останній рядок
    lines = lines[:-1]

    with open(filename, 'w', encoding='UTF-8') as file:
        file.writelines(lines)

    print(f"Останній рядок видалено з файлу '{filename}'")
else:
    print(f"Файл '{filename}' порожній")