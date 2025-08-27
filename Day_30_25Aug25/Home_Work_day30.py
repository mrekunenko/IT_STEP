# Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
# 1. ім'я клієнта
# 2. баланс
# 3. валюта
# 4. словник з курсом валют(однаковий для всіх)
# Додайте методи:
# 1. вивід загальної інформації
# 2. перевірка чи відома валюта(якщо ні, викликати ValueError)
# 3. перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати окремим методом)
# 4. зміна валюти
# 5. поповнення балансу(валюта та сама)
# 6. зняття грошей з балансу(валюта та сама).

class BankAccount:
    # курс валют — один для всіх об'єктів
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.9,
        "UAH": 40.0
    }

    def __init__(self, client_name, balance, currency):
        self.client_name = client_name
        self.balance = balance
        self.currency = currency

    def show_info(self):
        print(f"Клієнт: {self.client_name}, баланс: {self.balance:.2f} {self.currency}")

    def check_currency(self, currency):
        if currency not in BankAccount.exchange_rates:
            raise ValueError(f"Валюта {currency} невідома!")

    def convert(self, amount, from_currency, to_currency):
        self.check_currency(from_currency)
        self.check_currency(to_currency)
        usd_amount = amount / BankAccount.exchange_rates[from_currency]
        return usd_amount * BankAccount.exchange_rates[to_currency]

    def change_currency(self, new_currency):
        self.balance = self.convert(self.balance, self.currency, new_currency)
        self.currency = new_currency
        print(f"Валюта змінена на {new_currency}. Новий баланс: {self.balance:.2f} {new_currency}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Поповнення: {amount} {self.currency}. Баланс: {self.balance:.2f} {self.currency}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів!")
        else:
            self.balance -= amount
            print(f"Знято: {amount} {self.currency}. Баланс: {self.balance:.2f} {self.currency}")


# 🔹 Тестування (поза класом!)
acc = BankAccount("Богдан", 1000, "USD")
acc.show_info()
acc.deposit(500)
acc.withdraw(200)
acc.change_currency("UAH")
acc.show_info()
