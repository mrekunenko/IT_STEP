"""
client.py
Консольний клієнт для взаємодії з локальним API фільмів.

Запуск:
    python client.py
"""

import requests

BASE_URL = "http://127.0.0.1:8000"


def print_movie(movie: dict) -> None:
    """
    Nicely print a single movie dictionary to console (Ukrainian messages).
    """
    print("------------------------")
    print(f"ID:        {movie.get('id')}")
    print(f"Назва:     {movie.get('title')}")
    print(f"Режисер:   {movie.get('director')}")
    print(f"Рік:       {movie.get('year')}")
    print("------------------------")


def action_get_movie() -> None:
    """
    Ask user for movie ID and send GET /movies/{id}.
    """
    try:
        movie_id = int(input("Введіть ID фільму: "))
    except ValueError:
        print("ID має бути числом.")
        return

    response = requests.get(f"{BASE_URL}/movies/{movie_id}")

    if response.status_code == 200:
        data = response.json()
        print_movie(data)
    else:
        print(f"Помилка {response.status_code}: {response.text}")


def action_get_all() -> None:
    """
    Send GET /movies and print all movies.
    """
    response = requests.get(f"{BASE_URL}/movies")

    if response.status_code == 200:
        data = response.json()  # expected to be a list
        if not data:
            print("База наразі порожня.")
        else:
            print(f"Знайдено {len(data)} фільм(и/ів):")
            for movie in data:
                print_movie(movie)
    else:
        print(f"Помилка {response.status_code}: {response.text}")


def action_add_movie() -> None:
    """
    Ask user for new movie data and send POST /movies.
    """
    try:
        movie_id = int(input("Введіть ID фільму (число): "))
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
        "id": movie_id,
        "title": title,
        "director": director,
        "year": year
    }

    response = requests.post(f"{BASE_URL}/movies", json=payload)

    if response.status_code == 201:
        print("Фільм успішно додано:")
        print_movie(response.json())
    else:
        print(f"Помилка {response.status_code}: {response.text}")


def action_delete_movie() -> None:
    """
    Ask user for movie ID and send DELETE /movies/{id}.
    """
    try:
        movie_id = int(input("Введіть ID фільму для видалення: "))
    except ValueError:
        print("ID має бути числом.")
        return

    response = requests.delete(f"{BASE_URL}/movies/{movie_id}")

    if response.status_code == 204:
        print("Фільм успішно видалено.")
    else:
        print(f"Помилка {response.status_code}: {response.text}")


def main_menu() -> None:
    """
    Show interactive menu loop.
    All prompts/messages are in Ukrainian.
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
            action_get_movie()
        elif choice == 2:
            action_get_all()
        elif choice == 3:
            action_add_movie()
        elif choice == 4:
            action_delete_movie()
        elif choice == 5:
            print("Вихід із клієнта...")
            break
        else:
            print("Невірний вибір. Введіть число від 1 до 5.")


if __name__ == "__main__":
    main_menu()
