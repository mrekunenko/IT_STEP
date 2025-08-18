# Завдання 1
# Створіть 2 списки чисел різної довжини.
# Створіть на їх основі списки з
# 1. Усіма числами з обох списків
# 2. Усіма числами з обох списків, але без повторень
# 3. Спільними числами для двох списків
# 4. Числа які є в першому, але немає в другому

# Створення двох списків
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

# 1. Усі числа з обох списків
all_numbers = a + b
print("Усі:", all_numbers)

# 2. Усі числа без повторень
no_duplicates = []
i = 0
while i < len(all_numbers):
    x = all_numbers[i]
    if x not in no_duplicates:
        no_duplicates.append(x)
    i += 1
print("Без повторів:", no_duplicates)

# 3. Спільні числа
common = []
i = 0
while i < len(a):
    x = a[i]
    if x in b and x not in common:
        common.append(x)
    i += 1
print("Спільні:", common)

# 4. Тільки в першому
only_in_a = []
i = 0
while i < len(a):
    x = a[i]
    if x not in b:
        only_in_a.append(x)
    i += 1
print("Тільки в першому:", only_in_a)

