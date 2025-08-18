# Завдання 1
# Напишіть функцію, яка відображає наступний текст:
# “Don’t let the noise of others’ opinions
# drown out your own inner voice.”
# Steve Jobs

def show_text():
    print("“Don’t let the noise of others’ opinions")
    print("drown out your own inner voice.”")
    print("Steve Jobs")

# Виклик функції
show_text()


# Завдання 2
# Напишіть функцію, яка отримує два числа та відображає
# усі парні числа між ними

def show_even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end=' ')
    print()  # Перехід на новий рядок після виводу

# Введення чисел користувачем
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

# Виклик функції
show_even_numbers(a, b)


# Завдання 3
# Напишіть функцію, яка відображає числа діапазону в
# зростаючому або спадаючому порядку.
# Функція отримує 3 аргументи: межі діапазону та булеву
# змінну:
# a) якщо вона True – порядок зростаючий
# b) якщо вона False – порядок спадаючий

def show_numbers_range(start, end, is_up):
    if is_up:
        for number in range(start, end + 1):
            print(number, end=' ')
    else:
        for number in range(end, start - 1, -1):
            print(number, end=' ')
    print()  # Перехід на новий рядок

a = int(input("Введіть початок діапазону: "))
b = int(input("Введіть кінець діапазону: "))
order = input("Зростаючий порядок? (так/ні): ").lower()

# Визначення логічної змінної
is_up = False
if order == 'так':
    is_up = True

# Виклик функції
show_numbers_range(a, b, is_up)


# Завдання 4
# Напишіть функцію, яка повертає найбільше серед 4-ох
# чисел. Числа передаються як параметри.

def find_max_of_four(a, b, c, d):
    return max(a, b, c, d)

x1 = int(input("Введіть перше число: "))
x2 = int(input("Введіть друге число: "))
x3 = int(input("Введіть третє число: "))
x4 = int(input("Введіть четверте число: "))

maximum = find_max_of_four(x1, x2, x3, x4)
print("Найбільше число:", maximum)


# Завдання 5
# Напишіть функцію, яка обчислює суму чисел в певному
# діапазоні. Межі діапазону передаються як параметри.
# Якщо межі неправильні(наприклад числа від 10 до 5) то
# поміняйте їх місцями.

def sum_range(a, b):
    # Перевірка та заміна меж місцями, якщо потрібно
    if a > b:
        a, b = b, a

    total = 0
    for number in range(a, b + 1):
        total += number

    return total

start = int(input("Введіть перше число (початок діапазону): "))
end = int(input("Введіть друге число (кінець діапазону): "))

result = sum_range(start, end)
print("Сума чисел у діапазоні:", result)


# Завдання 6
# Напишіть функцію, яка перевіряє чи є число простим.
# Число передається як параметр. Результатом має бути True або
# False.
# Число називають простим, якщо воно ділиться лише на
# себе та 1

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Введіть число: "))
if is_prime(number):
    print("Число є простим.")
else:
    print("Число НЕ є простим.")


# Завдання 7
# Напишіть функцію, яка перевіряє чи є шестизначне число
# «щасливим». Число передається як параметр. Результатом має
# бути True або False.
# Число називають «щасливим» якщо сума перших трьох
# цифр дорівнює сумі останніх трьох чисел. Наприклад, 123420
# – щасливе, бо 1+2+3 = 4+2+0, а число 723422 – не щасливе, бо
# 7+2+3 != 4+2+2

def is_lucky_number(number):

    str_number = str(number)

    # Перевіряємо чи це шестизначне число
    if len(str_number) != 6:
        return False

    # Сума перших трьох цифр
    first_half = int(str_number[0]) + int(str_number[1]) + int(str_number[2])

    # Сума останніх трьох цифр
    second_half = int(str_number[3]) + int(str_number[4]) + int(str_number[5])

    # Порівнюємо суми
    return first_half == second_half


# Введення числа користувачем
number = int(input("Введіть шестизначне число: "))

# Перевірка та вивід результату
if is_lucky_number(number):
    print(f"Число {number} є щасливим!")
else:
    print(f"Число {number} не є щасливим.")