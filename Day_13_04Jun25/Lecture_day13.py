# nums = [10, 12, 20, 5, 12]
#
# ind = int(input("Введіть індекс числа: "))
#
#
# if 0 <= ind < len(nums):
#     print(nums[ind])
# else:
#     print("індекс неправильний")

# список рядків

fruits = ['apple', 'pear', 'kiwi']

# ind = int(input("Введіть індекс фрукта: "))
#
# if 0 <= ind < len(fruits):
#     print(fruits[ind])
# else:
#     print("індекс неправильний")

# fruit = input("Введіть назву фрукта")
#
# if fruit in fruits:
#     ind = fruits.index(fruit)
#     print(ind)
# else:
#     print("Такого фрукта немає в списку")


# # зрізи
#
# text = 'hello'
# char = 'e'
#
# print(text[0])   # 1 символ
# print(type(text[0]))
# print(text[:1])  # 1 символ
# print(type(text[:1]))
#
# nums = [1, 2, 3, 4]
# print(nums[0])  # число
# print(nums[:1]) # список з одним елементом
#
# num = nums[0]
# print(type(num))
# print(num + 10)
#
# num = nums[:1]
# print(type(num))
# print(num + 10)


# списки рядків

# text = 'apple, banana, kiwi, pear'
#
# # ріже текст на частини
# parts = text.split(", ")
#
# print(type(parts))
# print(parts)

# words = input("Введіть слова через пропуск ").split()


# # замінити в кожному слові букву а на А
# for i in range(len(words)):
#     words[i] = words[i].replace('а', "A")
#     word = words[i]
#
#     print(word)
#
# print(words)

# # вивести слова які мають менше 4 символів
# for word in words:
#     if len(word) < 4:
#         print(word)

# # вивести слова які написані в нижньому регістрі
# for word in words:
#     if word.islower():
#         print(word)

# for num in nums:
#     pass
#
# for user in users:
#     pass

# # замінити слова написані в нижньому регістрі на stop
# for i in range(len(words)):
#     # word = words[i]
#     #
#     # if word.islower():
#     #     words[i] = 'stop'
#
#     if words[i].islower():
#         words[i] = 'stop'
#
#
# # об'єднати слова в текст через ', '
# text = ', '.join(words)
# print(type(text))
# print(text)

# сортування
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

salaries = [
    3000, 3100, 2200, 2300, 2400, 2000,
    1900, 2000, 2500, 2600, 2700, 3200
]

salaries.sort(reverse=True) # від бульшого до меншого
print(salaries)

months.sort()
print(months)






# # Є два списки: назви місяців та зарплата співробітника.
# # Користувач вводить назву місяця. Ввиведіть зарплату
# # за цей місяць
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
# ]
#
# salaries = [
#     3000, 3100, 2200, 2300, 2400, 2000,
#     1900, 2000, 2500, 2600, 2700, 3200
# ]
#
# while True:
#     # інструкція
#     print("Введіть один з місяців або END для закінчення")
#     print("  ".join(months))
#
#     # введення даних
#     month = input('Введіть назву місяця: ').strip()
#
#     # strip -- видаляє лишні пропуски на початку та вкінці
#
#     # перевірка чи кінець
#     if month == "END":
#         break
#
#     # отримуємо перші 3 літери
#     month = month[:3].capitalize()
#
#     # чи правильний місяць
#     if month not in months: # якщо неправильний, починаємо заново
#         print("Неправильна назва місяця")
#         print()
#         continue
#
#     # вивід даних
#     ind = months.index(month)
#
#     salary = salaries[ind]
#
#     print(f'Зарплата за {month} -- {salary}')
#     print()
