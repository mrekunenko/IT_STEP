# # enumerate
#
# fruits = ['banana', 'apple', 'pear']
#
# for i, fruit in enumerate(fruits):
#     print(f"Індекс: {i}  елемент: {fruit}")
#
#
# for i in range(len(fruits)):
#     fruit = fruits[i]
#
#     print(f"Індекс: {i}  елемент: {fruit}")

# множини (set)
list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)
set1 = {1, 2, 3, 4}  # Shift + [

# # порожня множина
# # set1 = {}  # не працює, це не множина а словник
# set1 = set()
# print(type(set1))


# # зміни типів даних
# list1 = [1, 2, 3, 4]
# set1 = set(list1)
#
# tuple1 = (1, 2, 3, 4)
# set1 = set(tuple1)
#
# set1 = set("hello")
# print(set1)
#
# set1 = set(range(1, 10))
# print(set1)

# # генератори
# set1 = {num for num in range(10)}
# print(set1)


# множина містить лише унікальні елементи(без повторень)
set1 = {1, 1, 1, 4, 2, 2, 3, 4, 4, 1, 1, -100}

# print(set1)
# print(len(set1))

# мнодини не мають порядку, відповідно не мають індексів
# set1[0] -- помилка
# set1[1:3]

# # працює цикл for
# for item in set1:
#     print(item)

# # перевірка чи є елемент
# import time
#
#
# N = 10**7
# list1 = list(range(N))
# set1 = set(range(N))
#
# item = -1
#
# start = time.time()
# if item in list1:
#     pass
# end = time.time()
#
# print(f"Витрачено часу з list: {end - start}")
#
# start = time.time()
# if item in set1:
#     pass
# end = time.time()
#
# print(f"Витрачено часу з set: {end - start}")

# hash

# print(hash('apple'))
# print(hash('Apple'))
#
# set1 = {'apple', 'kiwi', 'pear'}
#
# print(hash((1, 2)))
# print(hash((1, 2, 3)))

# # хешуються лише незмінювальні типи даних
# # int, float, str, tuple
# nums = [1, 2]
#
# set1 = {nums, 12, 23}  # помилка
#
# if nums in set1:
#     pass
#
# nums.append(3)
#
# if nums in set1:
#     pass

# операції
set1 = {1, 2, 3}

# перевірка си є елемент
if 1 in set1:
    pass

if 2 not in set1:
    pass

# # добавити елемент
# set1.add(4)
# print(set1)
#
# set1.add(4)
# print(set1)

# # видалення елемента
# set1.discard(2)
# print(set1)
#
# set1.discard(-100) # немає помилки
# print(set1)


# операції з множинами

workers = ["Анна", "Олег", "Ігор", "Олег", "Анна", "Марія", "Сергій", "Олег"]
special_workers = ["Анна", "Ігор", "Вікторія"]  # працівники з особливим доступом

workers = set(workers)
special_workers = set(special_workers)

# вивести усіх працівників
# об'єднання множин
#all_workers = workers.union(special_workers)
all_workers = workers | special_workers
all_workers = special_workers | workers

print(all_workers)

# вивести працівників які не мають спеціального доступу
# різниця множин
#no_special_workers = workers.difference(special_workers)
no_special_workers = workers - special_workers
print(no_special_workers)

# інший результат
# no_special_workers = special_workers - workers
# print(no_special_workers)

# перетин множин
# елементи які є в обох одночасно
#both = workers.intersection(special_workers)
both = workers & special_workers

print(both)
