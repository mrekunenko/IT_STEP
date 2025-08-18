# # файли
# filename = "my_file.txt"
#
# # створення змінної file
# file = open(
#     filename,  # шлях\назва файлу
#     'r',     # для чого відкрити файл(r -- read)
# )
#
# # прочитати вміст файлу
# text = file.read()
#
# print(text)
#
# # після закінчення роботи треба закрити файл
# file.close()


# # те саме, але простіше
# # file = open(...)
# with open('my_file.txt', 'r') as file:
#     text = file.read()
# # закінчення блоку with -- файл автоматично закривається
#
# print(text)
#
# # інші методи читання
#
# with open('my_file.txt', 'r') as file:
#     lines = file.readlines()  # список рядків файлу
#
# print(lines)


# # для кирилиці
# with open('my_file.txt', 'r', encoding='UTF-8') as file:
#     text = file.read()
#
# print(text)

# режим для файлів(mode)
# r -- read(для читання)
# w -- write(для запису)
# a -- append(добавити)
# r+ -- для читання і запису

# with open('my_file.txt', 'r', encoding='UTF-8') as file:
#     text = file.read()
#
# print(text)


# # запис у файл
# # якщо файла не існує -- то він створиться
# # якщо існує -- очиститься
# with open('new_file.txt', 'w') as file:
#     file.write('Hello world\n')
#
# with open('new_file.txt', 'a') as file:
#     file.write('New line of text')


# # запис через print
# with open('new_file.txt', 'w') as f:
#     # f.write('Hello world\n')
#     print('New line', file=f)


# користувач вводить назву файлу. Вивести такі дані
# кількість символів
# кількість рядків
# кількість букв h
# збережіть статистику у новий файл

filename = input("введіть назву файлу: ")

with open(filename, 'r', encoding='UTF-8') as f:
    #text = f.read()
    lines = f.readlines()

# print(text)
# print(lines)

# кількість символів
total = 0
for line in lines:
    # видалити \n
    line = line.replace('\n', '')

    total += len(line)

# кількість букв h
count_h = 0
for line in lines:
    count_h += line.lower().count('h')


# назва файлу з результатами
# {user_filename}_results.txt

#new_filename = filename.replace('.txt', "_results.txt")
new_filename = filename[:-4] + "_results.txt"

# збереження даних у файл
with open(new_filename, 'w', encoding='UTF-8') as f:
    print(f"Загальна кількість символів: {total}", file=f)
    print(f"Кількість рядків: {len(lines)}", file=f)
    print(f"Кількість букв h: {count_h}", file=f)

print(f"Результати збережені у файл {new_filename}")

