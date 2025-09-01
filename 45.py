# Завдання 4. Квестова гра
# Створіть наступні класи:
#
# Warrior – атрибути name, health, attack
#
# Mage – атрибути name, health, mana
#
# Archer – атрибути name, health, arrows
#
# Методи:
#
# attack() – виводить повідомлення про атаку (залежно від типу героя)
#
# is_alive() – перевіряє, чи здоров’я > 0
#
# Напишіть функцію create_hero(), яка запитує у користувача тип героя та його характеристики і повертає об’єкт.
# Створіть команду героїв, добавте у список і змусьте їх зробити кілька дій.
#
# Завдання 5. Онлайн-магазин
# Створіть наступні класи:
#
# Product – атрибути name, price
#
# Customer – атрибути name, balance
#
# Cart – атрибути owner, items (список продуктів)
#
# Методи:
#
# add_product(product) – додає товар у кошик
#
# checkout() – знімає з балансу покупця вартість усіх товарів (якщо грошей вистачає)
#
# show_cart() – виводить список товарів і їх загальну вартість
#
# Напишіть функцію create_customer() та create_product(), які повертають об’єкти.
# Створіть кілька товарів, покупців і дайте їм зробити покупки.
#
# Завдання 6. Подорож
# Створіть наступні класи:
#
# City – атрибути name, country
#
# Hotel – атрибути name, stars, price_per_night
#
# Tourist – атрибути name, budget, current_city
#
# Методи:
#
# check_in(hotel, nights) – знімає гроші з бюджету туриста за проживання
#
# travel(new_city) – змінює місто, в якому перебуває турист
#
# info() – виводить інформацію про туриста, його бюджет і локацію
#
# Напишіть функцію create_tourist(), яка повертає об’єкт.
# Створіть кількох туристів, готелі та міста. Зробіть “подорож” з переїздами і поселенням у готелі.

class Warrior:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_action(self):
        return f"{self.name} (Воїн) завдає {self.attack} шкоди мечем!"

    def is_alive(self):
        return self.health > 0


class Mage:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana

    def attack_action(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} (Маг) кастує заклинання! Залишилось мани: {self.mana}"
        else:
            return f"{self.name} (Маг) не має достатньо мани для заклинання!"

    def is_alive(self):
        return self.health > 0


class Archer:
    def __init__(self, name, health, arrows):
        self.name = name
        self.health = health
        self.arrows = arrows

    def attack_action(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} (Лучник) стріляє стрілою! Залишилось стріл: {self.arrows}"
        else:
            return f"{self.name} (Лучник) залишився без стріл!"

    def is_alive(self):
        return self.health > 0


def create_hero():
    print("Створення героя:")
    print("1. Воїн")
    print("2. Маг")
    print("3. Лучник")

    hero_type = input("Оберіть тип героя (1-3): ")
    name = input("Введіть ім'я героя: ")
    health = int(input("Введіть здоров'я героя: "))

    if hero_type == "1":
        attack = int(input("Введіть силу атаки: "))
        return Warrior(name, health, attack)
    elif hero_type == "2":
        mana = int(input("Введіть кількість мани: "))
        return Mage(name, health, mana)
    elif hero_type == "3":
        arrows = int(input("Введіть кількість стріл: "))
        return Archer(name, health, arrows)
    else:
        print("Неправильний вибір!")
        return None


