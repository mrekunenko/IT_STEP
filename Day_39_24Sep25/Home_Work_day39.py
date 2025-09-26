# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
# 1. почати нову гру – користувач вводить числа до
# правильної відповіді
# 2. вивести результат – кількість перемог та програшів
# 3. зберегти дані – зберегти кількості перемог та
# програшів у файл
# 4. завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями

# guess_game_beginner.py
import json
import random
from typing import Tuple


class GameStats:
    """Клас для підрахунку перемог і поразок.

    Атрибути:
        wins (int): кількість перемог користувача.
        losses (int): кількість поразок користувача.
    """

    def __init__(self, wins: int = 0, losses: int = 0) -> None:
        self.wins = int(wins)
        self.losses = int(losses)

    def __repr__(self) -> str:
        return f"GameStats(wins={self.wins}, losses={self.losses})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GameStats):
            return False
        return self.wins == other.wins and self.losses == other.losses

    def to_dict(self) -> dict:
        return {"wins": self.wins, "losses": self.losses}

    @staticmethod
    def from_dict(data: dict) -> "GameStats":
        wins = int(data.get("wins", 0))
        losses = int(data.get("losses", 0))
        return GameStats(wins=wins, losses=losses)


def evaluate_winner(attempts: int) -> str:
    """Визначити переможця за кількістю спроб."""
    if attempts < 5:
        return "user"
    return "computer"


def save_stats(stats: GameStats, path: str = "stats.json") -> None:
    """Зберегти статистику у JSON-файл."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(stats.to_dict(), f, ensure_ascii=False, indent=2)


def load_stats(path: str = "stats.json") -> GameStats:
    """Завантажити статистику з JSON-файлу. Якщо файлу нема — повернути 0/0."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return GameStats.from_dict(data)
    except FileNotFoundError:
        return GameStats()
    except json.JSONDecodeError:
        # Пошкоджений файл → почати з нуля
        return GameStats()


def read_int(prompt: str) -> int:
    """Надійне читання цілого числа з підказкою."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
            return value
        except ValueError:
            print("Будь ласка, введіть ціле число.")


def play_single_game(secret: int | None = None) -> Tuple[str, int]:
    """Провести одну гру та повернути (переможець, кількість спроб)."""
    if secret is None:
        secret = random.randint(1, 100)

    attempts = 0
    print("Я загадав число від 1 до 100. Спробуй вгадати!")

    while True:
        guess = read_int("Введіть число: ")
        if guess < 1 or guess > 100:
            print("Число має бути в діапазоні 1..100.")
            continue

        attempts += 1
        if guess == secret:
            print(f"Вітаю! Ви вгадали число {secret} за {attempts} спроб(и).")
            break
        elif guess < secret:
            print("Моє число БІЛЬШЕ.")
        else:
            print("Моє число МЕНШЕ.")

    winner = evaluate_winner(attempts)
    if winner == "user":
        print("Переміг КОРИСТУВАЧ")
    else:
        print("Переміг КОМП'ЮТЕР")
    return winner, attempts


def show_result(stats: GameStats) -> None:
    """Вивести статистику."""
    print(f"Перемоги: {stats.wins} | Програші: {stats.losses}")


def main_menu() -> None:
    """Головне меню застосунку."""
    stats = load_stats()  # спробуємо підхопити попередні результати

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Нова гра")
        print("2. Показати результат")
        print("3. Зберегти дані")
        print("4. Завантажити дані")
        print("5. Вихід")

        choice = read_int("Ваш вибір: ")

        if choice == 1:
            winner, _ = play_single_game()
            if winner == "user":
                stats.wins += 1
            else:
                stats.losses += 1
        elif choice == 2:
            show_result(stats)
        elif choice == 3:
            save_stats(stats)
            print("Дані збережено у файл stats.json.")
        elif choice == 4:
            stats = load_stats()
            print("Дані завантажено.")
        elif choice == 5:
            print("Бувайте!")
            break
        else:
            print("Невірний пункт меню. Спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()
