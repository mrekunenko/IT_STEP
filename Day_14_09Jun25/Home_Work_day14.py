# Завдання 1.
# Напишіть гру «Wordy». Є загадане комп’ютером слово з 5-ти літер, здача користувача вгадати його.
# Користувач по черзі вводить свої варіанти відповіді після чого показується статистика:
# a) скільки літер правильні і стоять в правильному місці;
# b) скільки літер правильні, але стоять в неправильному місці;
# Гра продовжується поки користувач не вгадає слово, або не введе END (в цьому випадку показати загадане слово).

import random

# Список слів з 5 літер
words = ["apple", "table", "house", "mouse", "light", "water", "grape", "happy", "music", "paper"]

# Випадковий вибір слова
secret = random.choice(words)
attempt = 1

while True:
    guess = input("Введіть слово: ").lower()

    if guess == secret:
        print("Вітаю! Ви вгадали!")
        break

    if guess == "end":
        print(f"Загадане слово: {secret}")
        break

    # Літери на правильних місцях
    correct = 0
    for i in range(5):
        if guess[i] == secret[i]:
            correct += 1

    # Загальна кількість правильних літер
    in_word = 0
    for char in set(guess):
        in_word += min(guess.count(char), secret.count(char))

    # Літери не на своїх місцях
    wrong = in_word - correct

    print(f"На місці: {correct}, Не на місці: {wrong}")