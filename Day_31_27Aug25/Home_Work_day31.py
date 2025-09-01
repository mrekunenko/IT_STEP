# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.


class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата карткою {amount}{self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal {amount}{self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount}{self.currency}")


# Функція для створення платіжного об'єкта
def create_payment():
    """функцію create_payment() яка запитує у
користувача тип рахунку та потрібні атрибути й повертає
об'єкт."""
    while True:  # Додано цикл для повторного запиту при помилці
        payment_type = input("Введіть тип платежу (card/paypal/crypto): ").lower()
        currency = input("Введіть валюту (наприклад USD, EUR, UAH): ")

        if payment_type == "card":
            return CreditCardPayment(currency)
        elif payment_type == "paypal":
            return PayPalPayment(currency)
        elif payment_type == "crypto":
            return CryptoPayment(currency)
        else:
            print("Невідомий тип платежу! Спробуйте ще раз.")

"""Створіть декілька рахунків, добавте їх у список та для
кожної викличте відповідні методи."""
payments = []

# створимо кілька об'єктів через функцію
for i in range(3):
    print(f"Створення рахунку {i+1}:")
    payment = create_payment()
    payments.append(payment)

# викликаємо методи pay для кожного
for i, p in enumerate(payments, 1):
    while True:  # Додано перевірку введення суми
        try:
            amount = int(input(f"Введіть суму для оплати (рахунок {i}): "))
            p.pay(amount)
            break
        except ValueError:
            print("Введіть коректну суму!")