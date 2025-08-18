# Завдання 1
# Напишіть програму для роботи онлайн магазину.
# Товари:
# 1. подушка – 450 грн
# 2. ковдра – 1200 грн
# 3. лампа – 500 грн
# 4. брилок – 60 грн
# Меню:
# 1. додати товар
# 2. видалити товар
# 3. очистити кошик
# 4. показати суму покупки
# 5. вихід
# В залежності від вибору користувача, програма просить
# ввести назву товару та його кількість.


# Ціни товарів
tsina_podushka = 450
tsina_kovdra = 1200
tsina_lampa = 500
tsina_brylok = 60

# Кількість товарів у кошику
kilkist_podushka = 0
kilkist_kovdra = 0
kilkist_lampa = 0
kilkist_brylok = 0

while True:
    # Меню дій
    print(" ")
    print("1. Додати товар")
    print("2. Видалити товар")
    print("3. Очистити кошик")
    print("4. Показати суму покупки")
    print("5. Вихід")

    vybir = input("Ваш вибір (1-5): ")

    if vybir == "1":
        # Додавання товару
        print("\nДоступні товари:")
        print("1. Подушка - 450 грн")
        print("2. Ковдра - 1200 грн")
        print("3. Лампа - 500 грн")
        print("4. Брилок - 60 грн")

        tovar = input("Введіть товар (подушка, ковдра, лампа, брилок): ")
        kilkist = int(input("Введіть кількість: "))

        if tovar == "подушка":
            kilkist_podushka += kilkist
        elif tovar == "ковдра":
            kilkist_kovdra += kilkist
        elif tovar == "лампа":
            kilkist_lampa += kilkist
        elif tovar == "брилок":
            kilkist_brylok += kilkist
        else:
            print("Такого товару немає в магазині!")

    elif vybir == "2":
        # Видалення товару (обнуляємо кількість)
        tovar = input("Який товар видалити (подушка, ковдра, лампа, брилок)? ")
        if tovar == "подушка":
            kilkist_podushka = 0
        elif tovar == "ковдра":
            kilkist_kovdra = 0
        elif tovar == "лампа":
            kilkist_lampa = 0
        elif tovar == "брилок":
            kilkist_brylok = 0
        else:
            print("Товар не знайдено")

    elif vybir == "3":
        # Очищення кошика
        kilkist_podushka = 0
        kilkist_kovdra = 0
        kilkist_lampa = 0
        kilkist_brylok = 0
        print("Кошик очищено!")

    # Показати суму покупки
    elif vybir == "4":
        suma = 0
        suma += kilkist_podushka * tsina_podushka
        suma += kilkist_kovdra * tsina_kovdra
        suma += kilkist_lampa * tsina_lampa
        suma += kilkist_brylok * tsina_brylok
        print(f"Загальна сума: {suma} грн")

    # Вихід з програми
    elif vybir == "5":
        print("Дякуємо за покупки!")
        break
    else:
        print("Невірний вибір! Спробуйте ще раз.")
