import random

# Константи
CROSS = 'X'
ZERO = 'O'

def symbol_choice():
    """
    Функція для вибору символів гравців у грі "Хрестики-нулики".

    1. Запитує імена двох користувачів.
    2. Запитує, за яку фігуру (CROSS або ZERO) хоче грати кожен.
    3. Якщо обидва вибрали один і той самий символ — програма випадково призначає символи гравцям
       і повідомляє про це.
    4. Повертає два списки:
        - names: список з іменами гравців
        - symbols: список з відповідними символами для кожного гравця

    Повертає:
        tuple[list[str], list[str]]: (names, symbols)
    """
    # Запит імен користувачів
    name1 = input("Введіть ім'я першого гравця: ")
    name2 = input("Введіть ім'я другого гравця: ")

    # Запит символів
    symbol1 = input(f"{name1}, обери символ ({CROSS} або {ZERO}): ").upper()
    symbol2 = input(f"{name2}, обери символ ({CROSS} або {ZERO}): ").upper()

    # Якщо символи однакові — призначення випадкове
    if symbol1 == symbol2:
        print("Обидва гравці обрали один і той самий символ.")
        symbols = [CROSS, ZERO]
        random.shuffle(symbols)
        symbol1, symbol2 = symbols
        print(f"{name1} тепер грає '{symbol1}', а {name2} — '{symbol2}'")

    # Повертаємо списки
    names = [name1, name2]
    symbols = [symbol1, symbol2]
    return names, symbols