# Завдання 1 Є текстовий файл. Виведіть кількість рядків та кількість символів в ньому

filename = input("Введіть назву файлу: ")

with open(filename, 'r', encoding='UTF-8') as file:
    text = file.read()
    lines = text.splitlines()

print(f"Кількість рядків: {len(lines)}")
print(f"Кількість символів: {len(text.replace('\n', ''))}")


# Завдання 2
# Користувач вводить ім’я та вік. Запишіть їх у файл. Назву
# файлу також вводить користувач(без розширення .txt)

name = input("Введіть ім'я: ")
age = input("Введіть вік: ")
file_name = input("Введіть назву файлу (без .txt): ").strip() + ".txt"

with open(file_name, 'w', encoding='utf-8') as f:
    f.write(f"Ім'я: {name}\n")
    f.write(f"Вік: {age}\n")

print(f"Дані збережені у файл {file_name}")


# Завдання 3
# Є текстовий файл. Запишіть його рядки в інший файл.

source_filename = input("Введіть назву файлу для читання: ")
target_filename = input("Введіть назву файлу для запису: ")

with open(source_filename, 'r', encoding='UTF-8') as source, \
        open(target_filename, 'w', encoding='UTF-8') as target:
    target.writelines(source.readlines())

print(f"Файл скопійовано!")



#Завдання 4
#Завдання 4
# Користувач вводить літеру та назву файлу. Виведіть усі
# слова з файлу, які починаються на цю літеру.


letter = input("Введіть літеру: ").lower()
filename = input("Введіть назву файлу: ").strip()

with open(filename, 'r', encoding='utf-8') as f:
    words = f.read().split()

for word in words:
    if word.lower().startswith(letter):
        print(word)

# Завдання 5
# Є текстовий файл. Замініть у ньому усі символи * на &, та
# навпаки.

filename = input("Введіть назву файлу: ").strip()

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('*', '#TEMP#')
text = text.replace('&', '*')
text = text.replace('#TEMP#', '&')

with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)

print("Заміна виконана.")


# Завдання 6
# Напишіть функцію, яка отримує назву файлу та список
# чисел як параметри. Потрібно записати всі числа у файл,
# розмістивши кожне число на окремому рядку.

def save_numbers(filename, numbers):
    with open(filename, 'w', encoding='utf-8') as f:
        for num in numbers:
            f.write(str(num) + '\n')


file_name = input("Введіть назву файлу: ").strip()
nums = [1, 5, 9, 12, 45]

save_numbers(file_name, nums)
print("Числа записані у файл.")


#
