# Завдання 1
# Напишіть функцію, яка повертає добуток чисел з списку.
# Список передається як параметр.

def dobutok_spysku(spysok):
    dobutok = 1
    for chyslo in spysok:
        dobutok *= chyslo
    return dobutok


miy_spysok = [2, 3, 4]
rezultat = dobutok_spysku(miy_spysok)
print("Добуток чисел:", rezultat)



# Завдання 2
# Напишіть функцію, яка повертає найменше число з
# списку. Список передається як параметр.

def naymenshe_chyslo(spysok):
    return min(spysok)


miy_spysok = [5, 2, 9, -3, 7]
print("Найменше число:", naymenshe_chyslo(miy_spysok))


# Завдання 3
# Напишіть функцію, яка повертає кількість парних
# чисел з списку. Список передається як параметр.

def kilkist_parnykh(spysok):
    kilkist = 0
    for chyslo in spysok:
        if chyslo % 2 == 0:
            kilkist += 1
    return kilkist


miy_spysok = [1, 4, 6, 7, 10]
print("Кількість парних чисел:", kilkist_parnykh(miy_spysok))


# Завдання 4
# Напишіть функцію, яка видаляє з списку певне число.
# Якщо число повторюється, то треба видалити всі входження.
# Функція повинна повернути кількість видалених елементів.
# Список та число передаються як параметри

def vydalyty_znachennia(spysok, chyslo):
    kilkist_do = len(spysok)
    spysok[:] = [x for x in spysok if x != chyslo]
    kilkist_pislia = len(spysok)
    return kilkist_do - kilkist_pislia


miy_spysok = [3, 5, 2, 5, 7, 5]
vidaleno = vydalyty_znachennia(miy_spysok, 5)
print("Оновлений список:", miy_spysok)
print("Кількість видалених:", vidaleno)



# Завдання 5
# Напишіть функцію, яка отримує два списи як параметри.
# Функція повинна об’єднати списки та повернути результат.
# Наприклад, якщо функція отримує списки [1, 2, 3] та [3, 4]
# то результатом має бути список [1, 2, 3, 3, 4]

def obiednaty_spysky(spysok1, spysok2):
    return spysok1 + spysok2


a = [1, 2, 3]
b = [3, 4]
rezultat = obiednaty_spysky(a, b)
print("Об'єднаний список:", rezultat)


# Завдання 6
# Напишіть функцію, яка підносить кожен елемент списку
# до степеня. Результатом має бути список з степенями всіх
# чисел. Список та показник степеня передаються як параметри.

def stupin_spysku(spysok, stepin):
    novyi_spysok = []
    for chyslo in spysok:
        novyi_spysok.append(chyslo ** stepin)
    return novyi_spysok


miy_spysok = [2, 3, 4]
rezultat = stupin_spysku(miy_spysok, 2)
print("Список у квадраті:", rezultat)



