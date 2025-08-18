# Завдання 1
# Користувач вводить рядок англійською мовою. Порахуйте
# скільки в ньому голосних літер(aeuio)

text = input("Enter a string: ").lower()

vowel_count = 0
vowels = "aeiou"

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")

# Завдання 2
# Користувач вводить текст.
# Після чого запускається цикл і користувач вводить певне
# слово. Треба це слово в тексті замінити на верхній регістр.
# Цикл закінчується коли введено EXIT
# Приклад:
# Текст – a big red fox is eating red apple
# Слово red – a big RED fox is eating RED apple
# Слово fox – a big RED FOX is eating RED apple
# Слово EXIT – кінець програми, показати результат

# Отримуємо початковий текст від користувача
text = input("Введіть текст: ")

while True:
    # Отримуємо слово для заміни
    word = input("Введіть слово для заміни (або EXIT для завершення): ")

    # Перевіряємо, чи користувач хоче вийти
    if word.upper() == "EXIT":
        break

    # Замінюємо слова у тексті на введені слова у верхньому регістрі
    text = text.replace(word, word.upper())

# Виводимо кінцевий результат
print("Результат:")
print(text)


# Завдання 3
# Користувач вводить текст. Порахуйте скільки в ньому речень

text = input("Введіть текст: ")

marks = [".", "!", "?"]
count = 0

for char in text:
    if char in marks:
        count += 1

print(f"Кількість речень у тексті: {count}")
