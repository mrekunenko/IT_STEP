result = max(1, 2, 10, 7)
print(f"Max: {result}")

#Завдання 1
#Користувач вводить свій вік. Виведіть рік, коли він народився

# Отримуємо вік користувача
age = int(input("Введіть ваш вік: "))
current_year = 2025

# Розраховуємо рік народження
birth_year = current_year - age

# Виведення результату
print(f"Ваш вік: {age} років")
print(f"Рік вашого народження: {birth_year}")


# Завдання 2
#Користувач вводить довжину ребра куба. Виведіть його об’єм.
# Формула об'єму куба: V = a³, де a - довжина ребра

# Отримуємо довжину ребра куба
rebro_length = float(input("Введіть довжину ребра куба: "))

# Обчислюємо об'єм куба
volume = rebro_length ** 3

# Виведення результату
print(f"Об'єм куба з довжиною ребра {rebro_length} дорівнює {volume:.3f}")


# Завдання 3
# Програма для збільшення числа на вказаний відсоток

# Отримуємо введені користувачем дані
chyslo = float(input("Введіть число: "))
vidsotok = float(input("Введіть відсоток: "))

# Розраховуємо результат
rezultat = chyslo + (chyslo * vidsotok / 100)

# Виводимо результат
print(f"{chyslo} збільшене на {vidsotok}% дорівнює {rezultat:.2f}")


#Завдання 4
#Користувач вводить два числа: ціле(int) та дробове(float).
#Обчисліть суму, добуток та частку

# Отримуємо введені користувачем дані
tsile_chyslo = int(input("Введіть ціле число: "))
drobove_chyslo = float(input("Введіть дробове число: "))

# Обчислюємо суму
suma = tsile_chyslo + drobove_chyslo

# Обчислюємо добуток
dobutok = tsile_chyslo * drobove_chyslo

# Обчислюємо частку
chastka = chastka = tsile_chyslo / drobove_chyslo

# Виводимо результати
print(f"Ціле число: {tsile_chyslo}")
print(f"Дробове число: {drobove_chyslo}")
print(f"Сума: {suma}")
print(f"Добуток: {dobutok}")
print(f"Частка: {chastka}")

# Завдання 5
# Користувач вводить радіус кола. Виведіть його площу. Вважайте що =3.1415
# Округліть результат до двох знаків після коми.

# π (пі)
PI = 3.1415

# Отримуємо радіус від користувача
radius = float(input("Введіть радіус кола: "))

# Обчислюємо площу кола за формулою S = π × r²
ploscha = PI * radius ** 2

# Округлюємо результат до двох знаків після коми
ploscha_okruglena = round(ploscha, 2)

# Виводимо результат
print(f"Радіус кола: {radius}")
print(f"Площа кола: {ploscha_okruglena}")


#Завдання 6
#Користувач вводить ціну однієї кружки та загальний бюджет.
#Обчисліть скільки кружок можна купити.
#Скільки грошей залишиться.

# Отримуємо ціну однієї кружки від користувача
tsina_kruzhky = float(input("Введіть ціну однієї кружки: "))

# Отримуємо загальний бюджет від користувача
byudzhet = float(input("Введіть загальний бюджет: "))

# Обчислюємо кількість кружок, які можна купити (цілочисельне ділення)
kilkist_kruzhok = byudzhet // tsina_kruzhky

# Обчислюємо залишок грошей
zalyshok = byudzhet % tsina_kruzhky

# Виводимо результати
print(f"За ціни {tsina_kruzhky} грн за кружку і бюджету {byudzhet} грн:")
print(f"Можна купити {int(kilkist_kruzhok)} кружок")
print(f"Залишиться {zalyshok} грн")


# Завдання 7
# Користувач вводить суму вкладу в банк та відсоток ставки.
# Обчисліть скільки користувач отримує через 5 років, якщо кожного року сума вкладу збільшується на даний відсоток
# Виведіть суму вкладу кожного року окремо

# Отримуємо суму вкладу від користувача
suma_vkladu = float(input("Введіть початкову суму вкладу: "))

# Отримуємо відсоток ставки від користувача
vidsotok = float(input("Введіть річний відсоток ставки: "))

# Виводимо початкову суму вкладу
print(f"Початкова сума вкладу: {suma_vkladu}")

# Обчислюємо та виводимо суму вкладу за кожен рік
potochna_suma = suma_vkladu

potochna_suma = potochna_suma + (potochna_suma * vidsotok / 100) # Рік 1
print(f"Сума вкладу після 1 року: {potochna_suma:.2f}")

potochna_suma = potochna_suma + (potochna_suma * vidsotok / 100) # Рік 2
print(f"Сума вкладу після 2 року: {potochna_suma:.2f}")

potochna_suma = potochna_suma + (potochna_suma * vidsotok / 100) # Рік 3
print(f"Сума вкладу після 3 року: {potochna_suma:.2f}")

potochna_suma = potochna_suma + (potochna_suma * vidsotok / 100) # Рік 4
print(f"Сума вкладу після 4 року: {potochna_suma:.2f}")

potochna_suma = potochna_suma + (potochna_suma * vidsotok / 100) # Рік 5
print(f"Сума вкладу після 5 року: {potochna_suma:.2f}")


# Завдання 8
# Користувач вводить довжину в метрах. Виведіть цю довжину в футах та ярдах.
# 1 метр = 3.2808399 фута
# 1 метр = 1.0936133 ярда

# Константи
METR_FUT = 3.2808399    # 1 метр = 3.2808399 фута
METR_YARD = 1.0936133   # 1 метр = 1.0936133 ярда

# Отримуємо довжину в метрах від користувача
dovzhyna_metr = float(input("Введіть довжину в метрах: "))

# Обчислюємо довжину в футах
dovzhyna_fut = dovzhyna_metr * METR_FUT

# Обчислюємо довжину в ярдах
dovzhyna_yard = dovzhyna_metr * METR_YARD

# Виводимо результати
print(f"{dovzhyna_metr} метрів = {dovzhyna_fut:.2f} футів")
print(f"{dovzhyna_metr} метрів = {dovzhyna_yard:.2f} ярдів")


# Завдання 9.
# Щоб спекти пиріг потрібно 4 яблука та 1.2 літра молока.
# Користувач вводить кількість яблук та молока(у літрах).
# Виведіть скільки він може спекти пирогів.
# Виведіть скільки яблук та молока залишиться.

# константи для одного пирога
yabluk_na_pirig = 4  # яблук
moloko_na_pirig = 1.2  # літрів

# введення даних від користувача
kilkist_yabluk = int(input("введіть кількість яблук: "))
kilkist_moloka = float(input("введіть кількість літрів молока: "))

# розрахунок максимальної кількості пирогів
pirogy_z_yablukami = kilkist_yabluk // yabluk_na_pirig
pirogy_z_molokom = kilkist_moloka // moloko_na_pirig

# визначення максимальної кількості пирогів
kilkist_pirogiv = min(pirogy_z_yablukami, pirogy_z_molokom)

# розрахунок залишків інгредієнтів
zalyshok_yabluk = kilkist_yabluk - (kilkist_pirogiv * yabluk_na_pirig)
zalyshok_moloka = kilkist_moloka - (kilkist_pirogiv * moloko_na_pirig)

# виведення результатів
print(f"можна спекти {int(kilkist_pirogiv)} пирогів")
print(f"залишиться {int(zalyshok_yabluk)} яблук")
print(f"залишиться {zalyshok_moloka:.1f} літрів молока")


# Завдання 10
# Користувач вводить кількість днів. виведіть скільки це років, тижнів та днів.
# Наприклад, 398 днів – 1рік 4 тижні 5 днів

# константи
dniv_v_roci = 365
dniv_v_tyzhni = 7

# отримання вхідних даних від користувача
kilkist_dniv = int(input("введіть кількість днів: "))

# розрахунок років
roky = kilkist_dniv // dniv_v_roci
zalyshok_dniv = kilkist_dniv % dniv_v_roci

# розрахунок тижнів
tyzhni = zalyshok_dniv // dniv_v_tyzhni
dni = zalyshok_dniv % dniv_v_tyzhni

# виведення результату
print(f"{kilkist_dniv} днів – {roky} років {tyzhni}тижнів {dni} днів")

