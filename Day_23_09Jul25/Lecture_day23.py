# словники

set1 = {'London', 'Kyiv'}
list1 = ['London', 'Kyiv']

items = ['молоко', 'яблуко']
prices = [30, 70]

# дані в словнику це пари(два знечення)
# key  value
# ключ та значення

prices = {
    'key': 'value',
    'молоко': 30,
    'яблуко': 70,
    'банани': 80
}

items[1] # елемент з індексом 1

# res = prices['яблуко']  # дістати значення за ключем 'яблуко'
# print(res)
#
# # ключі зберігаються так само як і в множинах, отже
# # 1 ключі будуть унікальні
# data = {
#     'молоко': 30,
#     'яблуко': 70,
#     'молоко': 80
# }
# print(data)
#
# # 2 ключі мають бути хешованими(незмінними)
# data = {
#     (1, 2): '',
#     'молоко': 30,
#     'яблуко': 70,
#     'молоко': 80
# }
#
# # значення -- обмежень немає
# data = {
#     'key1': 10,
#     'key2': 10,
#     'key3': [1, 2, 3, 4]
# }
#
# print(data)


# # створення
# # перерахувати всі пари у форматі ключ: значення
# data = {
#     'name': 'Anton',
#     'age': 25,
#     'email': 'anton@gail.com',
#     'grades': [12, 10, 11, 10]
# }
#
# # порожній словник
# data = {}
#
# # порожня множина
# set1 = set()
#
# # генератори
# list1 = [num*2 for num in range(10)]
# print(list1)
#
#
# items = ['молоко', 'яблуко', 'хліб']
# prices = [30, 70, 25]
# data = {item: price for item, price in zip(items, prices)}
#
# print(data)
#
# # зміни типів даних
# # помилка
# # list1 = [1, 2]
# # print(dict(list1))
#
# list1 = [
#     ('UK', 'London'),
#     ('France', 'Paris')
# ]
# print(dict(list1))
#
# print(dict(zip(items, prices)))

# операції

data = {
    'name': 'Anton',
    'age': 25,
    'email': 'anton@gail.com',
    'grades': [12, 10, 11, 10]
}

# # перевірка чи є ключ
#
# if 'name' in data:
#     print('є ключ name')
# else:
#     print('немає ключ name')
#
# # працює лише з ключами
# if 'anton@gail.com' in data:
#     print('є ключ anton@gail.com')
# else:
#     print('немає ключ anton@gail.com')
#
# # перевірити чи є таке значення
# if 'anton@gail.com' in data.values():
#     print('є значення anton@gail.com')
# else:
#     print('немає значення anton@gail.com')

# використання ключа

# res = data['email']
# print(res)
#
# # res = data['location']  # помилка
# # print(res)
#
#
# res = data.get('location', 'зачення якщо ключа немає')
# print(res)
#
# res = data.get('age', 'зачення якщо ключа немає')
# print(res)
#
# res = data.get('location')
# print(res)

# print(data)
#
# # добавити нову пару ключ:значення
# data['location'] = 'Kyiv'
#
# print(data)
#
# # змінити значення за ключем
# data['location'] = 'Kharkiv'
# data['age'] += 1
# print(data)
#
# # видалення
# grades = data.pop('grades')
# print(grades)
# print(data)

# цикл for

# for key in data:
#     print(key)
#
# for key, value in data.items():
#     print(f"{key} -- {value}")
#
# for value in data.values():
#     print(f"{value}")
#
# for key in data:
#     value = data[key]
#
#     print(value)

# напишуть функцію яка створює словник з інформацією про працівника
# (ім'я, зарплата, досвід)
# напишуть функцію яка створює список з інформацією про співробітників
# напишіть функцію яка збільшить зарплату працівникам які працюють більше 2 років

def get_employee_info():
    info = {}

    info['name'] = input("Введіть ім'я: ")
    info['salary'] = int(input("Введіть зарплату: "))
    info['expirience'] = int(input("Введіть досвід: "))

    return info


def get_all_employee_info(count):
    list_data = []
    dict_data = {}

    for _ in range(count):
        info = get_employee_info()

        list_data.append(info)

        name = info.pop('name')
        dict_data[name] = info

    return dict_data


def increase_salary(info):
    for name in info:
        # дані про співробітника name
        data = info[name]

        if data['expirience'] > 2:
            data['salary'] += 1



# #info = get_employee_info()
# info = get_all_employee_info(3)
#
# # гарний вивід словників
# import json
#
# print(json.dumps(info, indent=4))


info = {
    "Mary": {
        "salary": 3000,
        "expirience": 5
    },
    "Jhon": {
        "salary": 2000,
        "expirience": 1
    },
    "Anna": {
        "salary": 15000,
        "expirience": 10
    }
}

for key in info:
    print(key)

print(info['Anna']['salary'])