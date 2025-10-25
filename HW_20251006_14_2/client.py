"""
client.py
Простий клієнт командного рядка для взаємодії з API фільмів.

Запуск:
    python client.py

Можливості:
    1. Отримати дані про конкретний фільм за ID
    2. Отримати всі фільми
    3. Додати новий фільм
    4. Видалити фільм
    5. Вийти
"""

import requests

BASE_URL = "http://127.0.0.1:8000"


def надрукувати_фільм(фільм: dict) -> None:
    """
    Акуратно вивести один фільм.
    """
    print("------------------------")
    print(f"ID:        {фільм.get('id')}")
    print(f"Назва:     {фільм.get('title')}")
    print(f"Режисер:   {фільм.get('director')}")
    print(f"Рік:       {фільм.get('year')}")
    print("------------------------")


def отримати_фільм():
    """
    Запитує ID у користувача і робить GET /movies/{id}
    """
    try:
        film_id = int(input("Введіть ID фільму: "))
    except ValueError:
        print("ID має бути числом.")
        return

    resp = requests.get(f"{BASE_URL}/movies/{film_id}")

    if resp.status_code == 200:
        data = resp.json()
        надрукувати_фільм(data)
    else:
        print(f"Помилка {resp.status_code}: {resp.text}")


def отримати_всі():
    """
    Робить GET /movies і виводить усі фільми.
    """
    resp = requests.get(f"{BASE_URL}/movies")

    if resp.status_code == 200:
        data = resp.json()  # очікуємо список
        if not data:
            print("База порожня.")
        else:
            print(f"Знайдено {len(data)} фільм(и/ів):")
            for film in data:
                надрукувати_фільм(film)
    else:
        print(f"Помилка {resp.status_code}: {resp.text}")


def додати_фільм():
    """
    Запитує інформацію про новий фільм у користувача і робить POST /movies
    """
    try:
        film_id = int(input("Введіть ID фільму (число): "))
    except ValueError:
        print("ID має бути числом.")
        return

    title = input("Введіть назву фільму: ").strip()
    director = input("Введіть режисера: ").strip()

    try:
        year = int(input("Введіть рік виходу фільму: "))
    except ValueError:
        print("Рік має бути числом.")
        return

    payload = {
        "id": film_id,
        "title": title,
        "director": director,
        "year": year
    }

    resp = requests.post(f"{BASE_URL}/movies", json=payload)

    if resp.status_code == 201:
        print("Фільм успішно додано:")
        надрукувати_фільм(resp.json())
    else:
        print(f"Помилка {resp.status_code}: {resp.text}")


def видалити_фільм():
    """
    Запитує ID і робить DELETE /movies/{id}
    """
    try:
        film_id = int(input("Введіть ID фільму для видалення: "))
    except ValueError:
        print("ID має бути числом.")
        return

    resp = requests.delete(f"{BASE_URL}/movies/{film_id}")

    if resp.status_code == 204:
        print("Фільм успішно видалено.")
    else:
        print(f"Помилка {resp.status_code}: {resp.text}")


def головне_меню():
    """
    Нескінченний цикл вибору дій.
    """
    while True:
        print()
        print("Оберіть дію:")
        print("1. Отримати інформацію про фільм за ID")
        print("2. Отримати всі фільми")
        print("3. Додати новий фільм")
        print("4. Видалити фільм")
        print("5. Вийти")
        print()

        try:
            choice = int(input("Ваш вибір (1-5): "))
        except ValueError:
            print("Будь ласка, введіть число від 1 до 5.")
            continue

        if choice == 1:
            отримати_фільм()
        elif choice == 2:
            отримати_всі()
        elif choice == 3:
            додати_фільм()
        elif choice == 4:
            видалити_фільм()
        elif choice == 5:
            print("Вихід з клієнта...")
            break
        else:
            print("Невірний вибір. Введіть число від 1 до 5.")


if __name__ == "__main__":
    головне_меню()
