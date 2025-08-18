# # функція map
# # користувач вводить числа через кому, вивести їхню суму
#
# nums = input("Введіть числа через кому: ").split(', ')
#
# print(nums)
#
# # цикл for
# new_nums = []
# for num in nums:
#     new_nums.append(int(num))
#
# print(new_nums)
#
# # генератор
# # new_list = [item for...]
# new_nums = [int(num) for num in nums]
#
# # map
# new_nums = map(int, nums)
# new_nums = list(new_nums)
#
# print(new_nums)
#
# # об'єднати в один рядок
# new_nums = list(map(int, input("Введіть числа через кому").split(', ')))
#
# for num in new_nums:
#     print(num)

# кортежі
# # кортеж -- список, але без змін
# nums = [1, 2, 3]
# nums[1] = 100
# print(nums)

# # кортеж -- tuple
# nums = (1, 2, 3)
# print(nums)
# print(nums[1])

# # не можна вносити зміни
# nums[1] = 100

# методи count та index

# # проятись по циклу
# for num in nums:
#     print(num)
#
# for i in range(len(nums)):
#     print(nums[i])

# # зрізи
# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# print(nums[2:5])  # числа між індексом 2 та 5(не включно)
# print(nums[:4])  # перші 4 числа
# print(nums[-4:])  # останні 4 числа
# print(nums[-1])  # останній елемент
# print(nums[::-1])  # обернений порядок

# # створення кортежів
#
# words = ("pen", "pencil", "chalk")
# words = ("pen",)  # кортеж з одного елемента
# words = tuple()  # порожній кортеж
#
#
# print(type(words))
# print(words)
#
# # зміна типів даних
# result = tuple('apple')
# result = tuple(range(10))
#
# nums = [4, 5, 6, 2, 3]
# result = tuple(nums)
#
# print(result)
#
# # об'єднати елементи кортежу в str
# leters = ('a', 'p', 'p', 'l', 'e')
#
# result = ', '.join(leters)
# print(result)

# змінювальні типи даних -- list, set, dict
# незмінювальні -- int, float, str, tuple

# # присвоювання через розпаковку
# nums = (4, 5, 2)
#
# a, b, c = nums
#
#
# print(a)
# print(b)
# print(c)

data = [
    ('Ukraine', "Kyiv", 30),
    ("Spain", "Madrid", 45),
    ("UK", "London", 50)
]

# порахувати загальне населення та вивести всю інформацію
#
# total = 0
# for state, capital, population in data:
#     #state, capital, population = country
#     total += population
#     print(f"{state}: Столиця {capital}. Населення {population} млн")
#
# print(f"Загальне населення країн {total} млн")
#
# # інший варіант(генератор)
# total = sum(population for _, _, population in data)
# total = sum(country[-1] for country in data)
#
# print(f"Загальне населення країн {total} млн")

# # якщо з кортежа потрібно не все
# data = ('Ukraine', "Kyiv", 30)
#
# state, _, population = data
# _, capital, population = data

# отримання індекса та елемента послідавності

words = ["apple", 'banana', 'kiwi', 'pear']

# # цикл з індексом
# for i in range(len(words)):
#     word = words[i]
#
#     print(f"{i}. {word}")

# # enumerate
# for i, word in enumerate(words, start=1):  # індексація з 1
#     print(f"{i}. {word}")

# zip -- отримати пари з декількох списків
items = ["apple", 'banana', 'kiwi', 'pear', "hgljhljhj"]
prices = [20, 40, 50]
quantities = [2.5, 0.75, 0.5, 1.5]

# for item, price, quantity in zip(items, prices, quantities):
#     print(f"{item} -- загальна ціна {price*quantity}")

for data in zip(items, prices, quantities):
    print(data)

