# Завдання 1
# Напишіть функцію, яка отримує назву мови
# програмування та виводить повідомлення:
# «You are learning [мова програмування]»
# За замовчуванням, має бути Python.


def show_language(language="Python"):
    print(f"You are learning {language}")


lang = input("Enter programming language: ")
if lang == "":
    show_language()  # використає значення за замовчуванням
else:
    show_language(lang)


# Завдання 2
# Напишіть функцію, яка отримує текст як параметр та
# виводить його на екран. Також має бути параметр
# lowercase:
# a. Якщо він True, то текст потрібно перевести в
# нижній регістр
# b. Якщо False, то текст не змінюється
# За замовчуванням False.

def show_text(text, lowercase=False):
    if lowercase:
        text = text.lower()
    print(text)


user_text = input("Введіть текст: ")
user_option = input("Зробити нижній регістр? (так/ні): ")

make_lower = user_option.lower() == "так"
show_text(user_text, lowercase=make_lower)


# Завдання 3
# Напишіть функцію, яка отримує температуру та
# переводить її в градуси Цельсія або в Фаренгейта. Для
# цього є додатковий параметр unit_mapping:
# a. Якщо він C_to_F, то функція повинна повернути
# градуси Фаренгейта
# b. Якщо він F_to_C, то функція повинна повернути
# градуси Цельсія
# c.c. Якщо він щось інше, то функція виводить
# повідомлення про помилку, та повертає число без змін.
# За замовчуванням, C_to_F

def convert_temperature(temp, unit_mapping="C_to_F"):
    if unit_mapping == "C_to_F":
        return (temp * 9/5) + 32
    elif unit_mapping == "F_to_C":
        return (temp - 32) * 5/9
    else:
        print("Невірне значення unit_mapping. Повертаю без змін.")
        return temp


t = float(input("Введіть температуру: "))
direction = input("Напрямок конвертації (C_to_F або F_to_C): ")

result = convert_temperature(t, direction)
print(f"Результат: {result}")


# Завдання 4
# Напишіть функцію, яка отримує список чисел як
# параметр та повертає кількість парних або непарних
# чисел в ньому, в залежності від параметра odd:
# a. Якщо він True, то кількість непарних
# b. Якщо False, то кількість парних
# За замовчуванням False.

def count_numbers(numbers, odd=False):
    if odd:
        return sum(1 for num in numbers if num % 2 != 0)
    else:
        return sum(1 for num in numbers if num % 2 == 0)


user_input = input("Введіть числа через пробіл: ")
nums = [int(n) for n in user_input.split()]

choice = input("Порахувати непарні числа? (так/ні): ")
odd_mode = choice.lower() == "так"

result = count_numbers(nums, odd=odd_mode)
print(f"Результат: {result}")


# Завдання 5
# Напишіть функцію, яка отримує декілька чисел як
# параметрів.
# a. Якщо числа 2, то повернути найбільше
# b. Якщо числа 3, то повернути суму
# c. Якщо чисел більше 3, то повернути їхній добуток

def process_numbers(*numbers):
    # Перевірка
    for num in numbers:
        if not isinstance(num, (int, float)):
            print("Всі аргументи мають бути числами")
            return None

    count = len(numbers)

    if count == 2:
        return max(numbers)
    elif count == 3:
        return sum(numbers)
    elif count > 3:
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        print("Потрібно передати мінімум 2 числа")
        return None