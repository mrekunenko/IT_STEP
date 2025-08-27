# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

class Cart:
    def __init__(self, client):
        self.client = client
        self.items = []

    def add_item(self, item):
        """
        Метод для додавання товару до кошика
        item - назва товару, який потрібно додати
        """
        self.items.append(item)
        print(f'{item} додано до кошика.')

    def remove_item(self, item):
        """
        Метод для видалення товару з кошика
        item - назва товару, який потрібно видалити
        """
        if item in self.items:
            self.items.remove(item)
            print(f'{item} видалено з кошика.')
        else:
            print(f'{item} намає у кошику.')

    def show_cart(self):
        """
        Метод для виведення інформації про кошик
        """
        print(f"\n--- Кошик клієнта: {self.client} ---")
        if self.items:
            print(f"Кількість товарів: {len(self.items)}")
            print("Список товарів:")
            for i, item in enumerate(self.items, 1):
                print(f"  {i}. {item}")
        else:
            print("Кошик порожній")
        print("-" * (len(f"--- Кошик клієнта: {self.client} ---")))

cart = Cart("Богдан")
cart.add_item("Хліб")
cart.add_item("Молоко")
cart.show_cart()
cart.remove_item("Хліб")
cart.show_cart()


# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.

class Phone:
    def __init__(self, number, battery_level=100):
        """
        Конструктор класу Phone
        number - номер телефону
        battery_level - рівень заряду батареї (за замовчуванням 100%)
        """
        self.number = number
        self.battery_level = battery_level

    def use_battery(self, percent):
        """
        Метод для зменшення заряду телефона
        usage - на скільки відсотків зменшити заряд
        """
        self.battery_level -= percent
        if self.battery_level < 0:
            self.battery_level = 0   # заряд не може бути від’ємним
        if self.battery_level < 20:
            print("Заряд низький!")
        print(f"Залишок заряду: {self.battery_level}%")

    def show_info(self):
        """
        Метод для виведення інформації про телефон
        """
        print(f"Телефон {self.number}, заряд: {self.battery_level}%")

phone = Phone("+380501234567", 50)
phone.show_info()
phone.use_battery(25)
phone.use_battery(10)
phone.show_info()
