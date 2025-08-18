# Завдання 1
# Користувач вводить слово та індекс. Замініть символ під
# цим індексом на *. Скористайтесь зрізами
# Приклади:
# hello 1 – h*llo
# hello 2 – he*lo

# Введення даних
word = input("Введіть слово: ")
index = int(input("Введіть індекс: "))

# Перевіряємо коректність індексу
if 0 <= index < len(word):
    # Використовуємо зрізи для заміни
    # [:index] - все до вибраного індексу
    # [index+1:] - все після вибраного індексу
    new_word = word[:index] + '*' + word[index+1:]
    print(f"Результат: {new_word}")
else:
    print(f"Помилка! Індекс {index} виходить за межі слова")


# Завдання 2
# Користувач вводить слово. Зробіть першу та останню літеру великою.

word = input("Введіть слово: ")

if len(word) == 0:
    print("Порожній рядок")
elif len(word) == 1:
    print("Результат:", word.upper())
else:
    result = word[0].upper() + word[1:-1] + word[-1].upper()
    print("Результат:", result)


# Завдання 3
# Користувач вводить слова, поки не введе END. Виведіть в
# кінці ті слова, які починаються і закінчуються на одну і ту
# саму літеру.
# Приклади: око, дід, Ротор, Ангора

result = []

while True:
    word = input("Введіть слово (або END для завершення): ")

    if word.upper() == "END":
        break

    lower_word = word.lower()

    if len(lower_word) >= 1 and lower_word[0] == lower_word[-1]:
        result.append(word)

print("\nСлова, що починаються і закінчуються на одну літеру:")
for word in result:
    print(word)
