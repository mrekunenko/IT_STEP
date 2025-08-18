# Завдання 6
# Напишіть функцію, яка отримує назву файлу та список
# чисел як параметри. Потрібно записати всі числа у файл,
# розмістивши кожне число на окремому рядку.
# Напишіть іншу функцію, яка отримує назву файл та читає
# з нього ці числа і повертає як список.

def write_numbers(filename, numbers):
    with open(filename, 'w', encoding='UTF-8') as f:
        for num in numbers:
            f.write(str(num) + '\n')

def read_numbers(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        return [int(line.strip()) for line in f.readlines()]


nums = [10, 20, 30, 40]
write_numbers('numbers.txt', nums)
print(read_numbers('numbers.txt'))


# Завдання 7
# Є 2 файли, запишіть у третій файл лише ті символи, які є в
# обох файлах одночасно

def write_common_chars(file1, file2, output_file):
    with open(file1, 'r', encoding='UTF-8') as f1:
        text1 = f1.read()
    with open(file2, 'r', encoding='UTF-8') as f2:
        text2 = f2.read()

    common_chars = set(text1) & set(text2)

    with open(output_file, 'w', encoding='UTF-8') as out:
        out.write(''.join(common_chars))


write_common_chars('file1.txt', 'file2.txt', 'common.txt')











# Завдання 8
# Є файл з текстом. Видаліть з нього усі неприйнятні слова.
# Список неприйнятних слів є в іншому файлі

def remove_unacceptable_words(text_file, bad_words_file, output_file):
    with open(text_file, 'r', encoding='UTF-8') as tf:
        text = tf.read()
    with open(bad_words_file, 'r', encoding='UTF-8') as bf:
        bad_words = set(bf.read().lower().split())

    filtered_words = [word for word in text.split() if word.lower() not in bad_words]

    with open(output_file, 'w', encoding='UTF-8') as out:
        out.write(' '.join(filtered_words))


remove_unacceptable_words('text.txt', 'bad_words.txt', 'clean_text.txt')
