# ascii

# sym = 'g'
#
# # отримати код символу
# ascii_code = ord(sym)
# print(ascii_code)
#
# # отримати символ за кодом
# symbol = chr(61)
# print(symbol)
#
# # порівняння символів за кодом
#
# sym1 = 'apple'
# sym2 = 'dog'
#
# if sym1 < sym2:  # ord(sym1) < ord(sym2)
#     print(f"{sym1} знаходиться раніше в таблиці за символ {sym2}")
# else:
#     print(f"{sym2} знаходиться раніше в таблиці за символ {sym1}")

# синтаксис функції print

# help(round)

# text = "text"
# help(text.replace)

# help(print)

# print(1, 2, 3, sep='-----')

# print('a', end='')
# print('b')

# for i in range(1, 10):
#     print(i, end=' ')
# print()
#
# print('hello')


# індексація

# text = "abcde"
#
# # <назва змінної>[<індекс>]
# index = 0
# sym = text[index]
# print(sym)

# text = "abcde"
#
# # цикл звичайний
# for sym in text:
#     print(sym, end=' ')
# print()
#
# # цикл по індекса
# for i in range(len(text)):
#     sym = text[i]
#     print(f"{i} -- {sym}", end='\n')
# print()


# for i in range(1, 10):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)

# слайси та від'ємні індекси

# text = 'abcde'
# i = -2  # другий символ з кінця
# sym = text[i]
# print(sym)


# text[start:end:step]
# кінець не включно

# text = 'Hello, world!'
#
# print(text[2:8])  # вивести символи з 2 індекса по 8 індекс
# print(text[2:])   # кінець за замовчування -- кінець рядка
# print(text[:2])   # перші 2 символи
# print(text[-2:])  # останні 2 символи
# print(text[:])    # увесь рядок(копія)
# print(text[2:8:2])  # вивести символи з 2 індекса по 8 індекс з кроком 2
# print(text[::2])   # коджен другий символ
# print(text[::-1])  # рядок задом наперед

# методи

text = 'Hello, world!'

index = text.index('l')
print(index)
