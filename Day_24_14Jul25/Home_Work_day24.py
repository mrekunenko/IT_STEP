# Завдання 1
# Є словник з курсами валют, де ключ – назва валюти,
# значення – курс до гривні. Користувач вводить назву валюти,
# суму та назву нової валюти, в яку треба перевести суму.
# Підказка 1: для того щоб перевести, скажімо, 10 доларів у
# євро, спочатку треба перевести 10 доларів у гривні, після чого
# гривні переводити у євро.
# Підказка 2: щоб можна було переводити долари у
# гривні(або гривні у долари), потрібно щоб у словнику була
# інформація скільки гривень в 1 гривні

# Словник курсів валют (кількість гривень за 1 одиницю валюти)
exchange_rates = {
    "гривня": 1.0,
    "долар": 37.5,
    "євро": 40.2,
    "злотий": 9.1,
    "фунт": 45.8
}


def convert_currency():
    """Конвертує суму з однієї валюти в іншу"""

    print("Доступні валюти:", ", ".join(exchange_rates.keys()))

    # Отримуємо вхідні дані
    from_currency = input("Введіть валюту, з якої конвертуємо: ").lower()
    if from_currency not in exchange_rates:
        print("Помилка: валюта не знайдена")
        return

    amount_input = input("Введіть суму: ")
    if not amount_input.replace('.', '').isdigit():
        print("Помилка: некоректна сума")
        return
    amount = float(amount_input)

    to_currency = input("Введіть валюту, в яку конвертуємо: ").lower()
    if to_currency not in exchange_rates:
        print("Помилка: валюта не знайдена")
        return

    # Конвертація через гривню
    uah_amount = amount * exchange_rates[from_currency]
    converted_amount = uah_amount / exchange_rates[to_currency]

    # Вивід результату
    print(f"\nРезультат: {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")


# Запуск програми
if __name__ == "__main__":
    convert_currency()


# Завдання 2
# Напишіть функцію, яка отримує 2 множини з іменами
# працівників, які працюють в офісі та віддалено. Виведіть на
# екран:
#  Імена усіх працівників
#  Імена працівників, які працюють і в офісі, і віддалено
#  Відсоток працівників, які працюють і в офісі, і віддалено

def analyze_employees(office_workers, remote_workers):
    """
    Аналізує працівників, які працюють в офісі та віддалено.

    Параметри:
    - office_workers: множина працівників офісу
    - remote_workers: множина працівників на віддаленій роботі
    """
    # a) Усі працівники
    all_workers = office_workers.union(remote_workers)
    print(f"a) Усі працівники: {', '.join(sorted(all_workers))}")

    # b) Працівники, які працюють і в офісі, і віддалено
    hybrid_workers = office_workers.intersection(remote_workers)
    print(f"b) Працівники з гібридним форматом: {', '.join(sorted(hybrid_workers)) if hybrid_workers else 'немає'}")

    # c) Відсоток гібридних працівників
    total_workers = len(all_workers)
    hybrid_count = len(hybrid_workers)
    percentage = (hybrid_count / total_workers * 100) if total_workers > 0 else 0

    print(f"c) Відсоток гібридних працівників: {percentage:.1f}%")


# Приклад використання
if __name__ == "__main__":
    # Приклад даних
    office = {"Іван", "Марія", "Олег", "Наталія", "Андрій"}
    remote = {"Марія", "Олег", "Сергій", "Анна", "Віктор"}

    print("Аналіз працівників:")
    analyze_employees(office, remote)
