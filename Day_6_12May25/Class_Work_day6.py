
# num = 10
# text = 'hello'
# num = -20
#
# age = None
# print(type(age))
#
# # if age > 0:
# #     print()
# # else:
# #     print()


# користувач замовляє морозиво
# 1 кулька морозива -- 20 грн
# можна купити сироп(за бажанням)
# карамельний -- 5 грн
# шоколадний -- 4 грн

# Якщо замовили більше 3 кульки та
# з сиропом(один будь який) -- знижка 10%

# amount_ice_cream = int(input("Введіть скільки кульок морозива: "))
#
# # ціна
# total = amount_ice_cream * 20
#
# # питаємо за сироп
#
# syrop_choice = input("чи хочете ви сироп? (так або ні) ")
#
# if syrop_choice == 'так':
#     # уточнюємо який саме сироп вона хоче
#     syrop_type = input('Який саме сироп ви хочете?(карамельний або шоколадний) ')
#
#     # ціна за сироп
#     if syrop_type == 'карамельний':
#         total = total + 5
#     elif syrop_type == 'шоколадний':
#         total = total + 4
#
# # Якщо замовили більше 3 кульки та
# # з сиропом(один будь який) -- знижка 10%
#
# if amount_ice_cream > 3 and syrop_choice == 'так':
#     discount = 0.1 * total
#     total = total - discount
#
# print(f'З вас {total} грн')



# варіант з None
# amount_ice_cream = int(input("Введіть скільки кульок морозива: "))
#
# syrop_choice = input("чи хочете ви сироп? (так або ні) ")
#
# if syrop_choice == 'так':
#     # уточнюємо який саме сироп вона хоче
#     syrop_type = input('Який саме сироп ви хочете?(карамельний або шоколадний) ')
# else:
#     syrop_type = None # людина не обрала жодного сиропу
#
#
# # ціна кульок морозива
#
# total = amount_ice_cream * 20
#
# # ціна за сироп
# if syrop_type == 'карамельний':
#     total = total + 5
# elif syrop_type == 'шоколадний':
#     total = total + 4
#
# # Якщо замовили більше 3 кульки та
# # з сиропом(один будь який) -- знижка 10%
#
# if amount_ice_cream > 3 and syrop_type != None:
#     discount = 0.1 * total
#     total = total - discount
#
# # Якщо замовили більше 2 кульки та
# # з шоколадним сиропом
#
# if amount_ice_cream > 2 and syrop_type == 'шоколадний':
#     print()
#
# # Якщо замовили більше 5 кульки та
# # без сиропу
#
# if amount_ice_cream > 5 and syrop_type == None:
#     print()








# Користувач вводить кількість товару, ціну за одиницю
# та відсоток знижки. Визначте суму до сплати

# amount_item = int(input('Введіть кількість товару '))
# price_per_item = int(input('Ціна за одиницю товару  '))
# percent = int(input('Відсоток знижки  '))
#
# # початкова ціна
# total = amount_item * price_per_item
#
# # знижка
# discount = total * (percent / 100)
# total = total - discount
# total -= discount  # робить те саме
#
# counter = 10
#
# counter += 2
#
# counter *= 1.5

# Завдання 6
# Користувач вводить назву товару. Програма повинна
# вивести на екран одну з двох фраз: «Дозволено до продажу»
# або «Заборонено до продажу». Зробіть додаткові перевірки в
# залежності від товару:
# Якщо це алкоголь або тютюн то спитайте його вік і
# перевірте чи він повнолітній.
# Якщо це ліки, спитайте чи є рецепт від лікаря.
# # Інші товари дозволено купувати усім


product_type = input("Ведіть тип товару ")

if product_type == 'алкоголь' or product_type == 'тютюн':
    age = int(input("Введіть свій вік "))

    if age >= 18:  # людина повнолітня
        print("Дозволено до продажу")
    else:
        print("Заборонено до продажу")

elif product_type == 'ліки':
    have_recipe = input('Чи є у вас рецепт від лікаря? ')

    if have_recipe == 'так':
        print("Дозволено до продажу")
    else:
        print("Заборонено до продажу")

else:
    print("Дозволено до продажу")

