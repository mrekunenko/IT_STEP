# Завдання 1
# Напишіть функцію, яка запитує користувача пароль та
# повертає його. Якщо пароль поганий, тобто менше 8 символів
# чи містить однакові символи то викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.

def get_password():
    password = input("Введіть пароль: ")

    if len(password) < 8:
        raise ValueError("Пароль має містити не менше 8 символів.")

    if len(set(password)) == 1:
        raise ValueError("Пароль не може складатись з однакових символів.")

    return password

try:
    pw = get_password()
    print(f"Ваш пароль прийнято: {pw}")
except ValueError as err:
    print(f"Помилка: {err}")
except Exception:
    print("Сталася інша помилка.")


# Завдання 2
# Є словник де ключ – логін, а значення – пароль. Напишіть
# функцію, яка запитує користувача логін та пароль. Якщо
# логіна немає в словнику, або невірний пароль, то викликати
# ValueError.
# Написати код try … except який використовує дану
# функцію.


users = {
    "admin": "admin123",
    "user1": "qwerty123",
    "mykola": "python2024"
}


def login(users):
    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if username not in users:
        raise ValueError("Користувача з таким логіном не існує.")

    if users[username] != password:
        raise ValueError("Невірний пароль.")

    return f"Вітаю, {username}!"


try:
    msg = login(users)
    print(msg)
except ValueError as err:
    print(f"Помилка: {err}")
except Exception:
    print("Сталася інша помилка.")
