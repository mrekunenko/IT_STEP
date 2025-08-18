# # списки
#
# # text = "anjfl123456"
# #
# # list_num = [15, 12, -8, 3]
# #
# # # створення
# # # nums
# # # prices
# # # ages
# # # years
# #
# # nums = [1, 2, 3, 4]
# # nums = [] # порожній список
# # nums = [10]  # список з одним елементом(10)
# #
# # # конвертація типів даних
# # # age = int(input())
# # # age = int('25')
# #
# # nums = list(range(10, 20))
# # print(nums)
# #
# # symbols = list("hello, world!")
# # print(symbols)
#
#
# # # створіть список з числами від 1 до 5,
# # # але помножте їх на 4
# # # [4, 8, 12, 16, 20]
# #
# # nums = []
# #
# # for num in range(1, 5+1):
# #     nums.append(num*4)  # добавити елемент в кінець списку
# #
# # print(nums)
# #
# # # генератор списків
# #
# # # list = [<вираз що добавити> for <змінна> in <інша послідовність> ]
# # nums = [num*4 for num in range(1, 5+1)]
# #
# # print(nums)
#
# # індексація
#
# nums = [15, 20, 18, -65]
#
# # print(nums[0]) # перший елемент -- 15
# # print(nums[2])
# # print(nums[-1]) # останній елемент
# # print(nums[-3]) # третій елемент з кінця
#
# # print(nums[1:3])
# # print(nums[:2])  # перші 2 елемента
# # print(nums[-2:])  # останні 2 елемента
# # print(nums[::-1])  # крок -1, вивести задом наперед
#
# nums = [8, 7, 15, 10]
#
# # проходження по всіх індексах
# for i in range(len(nums)):
#     print(nums[i])
#
# # вивести всі елементи крім 3 очтанніх
# for i in range(len(nums)-3):
#     print(nums[i])

# зміни елементів за індексом
# text = 'hello'
# # text[2] = '*'
# print(text[:1] + '*' + text[2:])

nums = [15, 20, 18, 9]

# # змінити елемент з індексом 3
# #nums[3] = -1
# nums[3] *= 10
#
# print(nums)

# nums = [15, 20, 18, 9]
# # збільшити кожен елемент списку на 10
#
# positive_nums = []
#
# for num in nums:
#     print(num)
#     num = num + 10
#
# for i in range(len(nums)):
#     nums[i] += 10
#
# print(nums)


# методи
nums = [15, 20, 18, 9, 20]

# довжина(кількість елементів)
len(nums)

# # добавити елемент в кінець списку
# nums.append(100)
# print(nums)

# # добавити елемент на будь-яке місце
# nums.insert(0, 100)
# print(nums)

# # видалити елемент
# nums.remove(20)
# print(nums)

# # видалити елемент за індексом
# nums.pop(2)
# print(nums)

# count
# index


# # перевірка чи є елемент в списку
# if 20 in nums:
#     print('20 є в списку')
# else:
#     print('20 немає в списку')




# Зарплата менеджера становить 200$ + відсоток від продажу:
# продаж до 500$ –3%, 500 –1000$ – 5%, понад 1000$ – 8%.
# Користувач вводить з клавіатури рівень продажу для трьох
# менеджерів. Визначте їхню зарплату, а також найкращого
# менеджера, нарахуйте йому премію 200$ та виведіть підсумки на
# екран.


# Користувач вводить з клавіатури рівень продажу для трьох менеджерів.

sales = []
for i in range(3):
    manager_sale = int(input("Введіть продажі для менеджера: "))
    sales.append(manager_sale)

# список зарплат менеджерів
salaries = [200, 200, 200]

# нарахування відсотків
for i in range(len(salaries)):
    # отримати рівень продаж для і-го менеджера
    manager_sale = sales[i]

    # відсоток
    if manager_sale < 500:
        percent = 3
    elif 500 <= manager_sale < 1000:
        percent = 5
    else:
        percent = 8

    # змінюємо зарплату менеджера
    #salaries[i] += salaries[i]*percent/100
    salaries[i] *= 1 + percent / 100

#найкращого менеджера, нарахуйте йому премію 200$

# максимальні продажі
max_sale = max(sales)

for i in range(len(salaries)):
    # перевіряємо чи продав цей менеджер найбільше
    if sales[i] == max_sale:
        salaries[i] += 200

print(salaries)
