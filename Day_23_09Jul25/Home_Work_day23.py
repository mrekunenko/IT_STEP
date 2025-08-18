def deposit_money(accounts):
    """Функція для поповнення рахунку"""
    name = input("Введіть ім'я клієнта: ")
    amount = float(input("Введіть суму для поповнення: "))

    if name in accounts:
        accounts[name] += amount
        print(f"Рахунок {name} поповнено на {amount}. Новий баланс: {accounts[name]}")
    else:
        accounts[name] = amount
        print(f"Створено новий рахунок для {name} з балансом {amount}")


def withdraw_money(accounts):
    """Функція для зняття коштів"""
    name = input("Введіть ім'я клієнта: ")

    if name not in accounts:
        print("Помилка: такого клієнта не існує")
        return

    amount = float(input("Введіть суму для зняття: "))

    if accounts[name] < amount:
        print("Помилка: недостатньо коштів на рахунку")
    else:
        accounts[name] -= amount
        print(f"З рахунку {name} знято {amount}. Залишок: {accounts[name]}")


def show_balance(accounts):
    """Функція для показу балансу"""
    name = input("Введіть ім'я клієнта: ")

    if name in accounts:
        print(f"Баланс клієнта {name}: {accounts[name]}")
    else:
        print("Помилка: такого клієнта не існує")


def main():
    """Головна функція програми"""
    accounts = {}  # Словник для зберігання рахунків

    while True:
        print("\nБанківська система")
        print("1. Поповнити рахунок")
        print("2. Зняти кошти")
        print("3. Переглянути баланс")
        print("4. Вийти")

        choice = input("Виберіть дію (1-4): ")

        if choice == "1":
            deposit_money(accounts)
        elif choice == "2":
            withdraw_money(accounts)
        elif choice == "3":
            show_balance(accounts)
        elif choice == "4":
            print("Дякуємо за використання нашої системи!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()