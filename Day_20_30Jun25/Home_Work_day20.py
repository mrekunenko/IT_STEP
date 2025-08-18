# Завдання 1
# Напишіть lambda-функції, які:
#  Множить число на -1
#  Перевіряє чи рядок непорожній


# 1. Множить число на -1
negate = lambda x: x * -1

# 2. Перевіряє, чи рядок непорожній
is_not_empty = lambda s: len(s) > 0


# Ввід числа
num = int(input("Введи число: "))
print("Помножене на -1:", negate(num))

# Ввід рядка
text = input("Введи рядок: ")
print("Рядок непорожній?", is_not_empty(text))


# Завдання 2
# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел, рахує середнє арифметичне та
# повертає список з числами, які більші за середнє
#  Отримує список слів та повертає список слів, в яких
# рівно 4 літери


# 1. Повертає числа, більші за середнє
def filter_above_average(numbers):
    avg = sum(numbers) / len(numbers)
    return list(filter(lambda x: x > avg, numbers))

# 2. Повертає слова довжиною рівно 4 літери
def filter_four_letter_words(words):
    return list(filter(lambda word: len(word) == 4, words))


# Ввід чисел
nums = list(map(int, input("Введи числа через пробіл: ").split()))
print("Числа більші за середнє:", filter_above_average(nums))

# Ввід слів
words = input("Введи слова через пробіл: ").split()
print("Слова з 4 літер:", filter_four_letter_words(words))


# Завдання 3
# Напишіть функцію, яка отримує літеру та список слів і
# знаходить слово зі списку, в якому найбільша кількість даної
# літери.

def word_with_most_letter(letter, words):
    return max(words, key=lambda word: word.lower().count(letter.lower()))


# Ввід літери та слів
letter = input("Введи літеру: ")
words = input("Введи слова через пробіл: ").split()

# Виклик функції
result = word_with_most_letter(letter, words)
print(f"Слово з найбільшою кількістю '{letter}':", result)
