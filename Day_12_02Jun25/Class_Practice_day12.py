# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# 1. Виведіть на екран елементи цього списку
# 2. Збільшіть кожне число в 3 рази та виведіть результат
# 3. Замініть усі числа більші 10 на 0 та виведіть результат

numbers = [1, 8, -5, 9]

numbers = [1, 8, -5, 9]
print("Список:", numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 3
print("×3:", numbers)

for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = 0
print("Після заміни:", numbers)


# Завдання 2
# Користувач вводить числа, поки не введе -1. Збережіть усі
# ці числа в список. Виведіть їхню кількість, суму, мінімальне,
# максимальне та середнє.

numbers = []

print("Вводьте числа (введіть -1 щоб завершити):")

while True:
    num = float(input("Введіть число: "))
    if num == -1:
        break
    numbers.append(num)

if numbers:
    count = 0
    total = 0
    min_num = numbers[0]
    max_num = numbers[0]

    for n in numbers:
        count += 1
        total += n
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n

    print("Числа:", numbers)
    print("Кількість:", count)
    print("Сума:", total)
    print("Мінімальне:", min_num)
    print("Максимальне:", max_num)
    print("Середнє:", total / count)
else:
    print("Чисел не введено.")


# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть два
# нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.


positives = []
negatives = []

print("Вводьте числа (введіть 0 щоб завершити):")

while True:
    n = float(input("Число: "))
    if n == 0:
        break
    if n > 0:
        positives.append(n)
    elif n < 0:
        negatives.append(n)

print("Додатні числа:", positives)
print("Від’ємні числа:", negatives)


# Завдання 4
# Допоможіть користувачу створити набір з унікальних
# чисел.
# Спочатку користувач вводить кількість чисел, після чого
# самі числа. Якщо число нове, то добавте його в список. Якщо
# число уже є в списку, виведіть повідомлення про це.
# Продовжуйте, поки не на збираєте потрібну кількість чисел.

numbers = []

n = int(input("Кількість унікальних чисел: "))

while len(numbers) < n:
    x = input("Число: ")
    if x in numbers:
        print("Це число вже є.")
    else:
        numbers.append(x)

print("Унікальні числа:", numbers)
