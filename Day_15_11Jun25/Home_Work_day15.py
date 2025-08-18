# Завдання 1
# Напишіть функцію, яка відображає наступний текст:
# “Don’t compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

def show_quote():
    print("“Don’t compare yourself with anyone in this world…")
    print("if you do so, you are insulting yourself.”")
    print("Bill Gates")

# Виклик функції
show_quote()


# Завдання 2
# Напишіть функцію, яка отримує два числа та відображає
# усі непарні числа між ними

def show_odd_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number, end=' ')
    print()  # Перехід на новий рядок

# Введення чисел користувачем
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

# Виклик функції
show_odd_numbers(a, b)


# Завдання 3
# Напишіть функцію, яка відображає числа діапазону з
# кінцем включно або без нього.
# Функція отримує 3 аргументи: межі діапазону та булеву
# змінну:
# a. якщо вона True – кінець включно
# b. якщо вона False – кінець невкючно

def display_range(start, end, include_end):
    if include_end:
        print(f"Діапазон від {start} до {end} (включно):")
        for num in range(start, end + 1):
            print(num, end=' ')
    else:
        print(f"Діапазон від {start} до {end} (невключно):")
        for num in range(start, end):
            print(num, end=' ')
    print()  # Перехід на новий рядок



# Завдання 4
# Напишіть функцію, яка повертає найменше серед 5-ти
# чисел. Числа передаються як параметри.

def find_min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)

x1 = int(input("Введіть перше число: "))
x2 = int(input("Введіть друге число: "))
x3 = int(input("Введіть третє число: "))
x4 = int(input("Введіть четверте число: "))

minimum = find_min_of_four(x1, x2, x3, x4)
print("Найбільше число:", minimum)


# Завдання 5
# Напишіть функцію, яка обчислює добуток чисел в
# певному діапазоні. Межі діапазону передаються як параметри.
# Якщо межі неправильні (наприклад числа від 10 до 5) то
# поміняйте їх місцями.

def multiply_range(a, b):
    if a > b:
        a, b = b, a

    result = 1
    for number in range(a, b + 1):
        result *= number

    return result

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

product = multiply_range(start, end)
print("Добуток чисел у діапазоні:", product)
