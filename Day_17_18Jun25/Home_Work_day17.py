# Завдання 1
# Напишіть функцію, яка отримує ім’я студента та
# виводить повідомлення:
# «You are welcome, [студент]»
# За замовчуванням, має бути ваше ім’я

def greet_student(name="Mykola"):
    print(f"You are welcome, {name}")


user_name = input("Введіть ім’я студента (або натисніть Enter): ")

if user_name == "":
    greet_student()  # використовується ім’я за замовчуванням
else:
    greet_student(user_name)


# Завдання 2
# Напишіть функцію, яка отримує два числа як
# параметр та тип операції, що з ними можна зробити:
# a. Якщо він add, то поверніть суму чисел
# b. Якщо diff, то поверніть різницю чисел
# c. Якщо mult, то поверніть добуток чисел
# d. Якщо щось інше, виведіть інформацію про помилку
# За замовчуванням add.

def calculate(num1, num2, operation="add"):
    if operation == "add":
        return num1 + num2
    elif operation == "diff":
        return num1 - num2
    elif operation == "mult":
        return num1 * num2
    else:
        print("Невідома операція")
        return None


a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть операцію (add, diff, mult): ")

if op == "":
    result = calculate(a, b)
else:
    result = calculate(a, b, op)

print(f"Результат: {result}")


# Завдання 3
# Напишіть функцію, яка отримує назву свята та імена
# декількох гостей. Виведіть кожному гостю
# повідомлення:
# «[ім’я], you are invited to [назва свята]»
# Якщо гостей немає, потрібно вивести повідомлення:
# «No guests»

def invite_guests(holiday, guests):
    if not guests:
        print("No guests")
    else:
        for name in guests:
            print(f"{name}, you are invited to {holiday}")


holiday_name = input("Введіть назву свята: ")
guest_input = input("Введіть імена гостей через кому (або нічого): ")
guest_list = [name.strip() for name in guest_input.split(",") if name.strip() != ""]
invite_guests(holiday_name, guest_list)
