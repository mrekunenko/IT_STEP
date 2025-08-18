# функції

print("Hello")
print("Програма працює")

# визначення функції
# def <назва функції>(параметри):
def my_func():
    print("Hello")
    print("Програма працює")

# виклик функції
# <назва функції>(параметри)
my_func()

print('-----------')

my_func()

параметри функції

# функція яка показує суму чисел
# def <назва функції>(параметр1, параметр2, ...):
def show_sum(num1, num2):
    summa = num1 + num2
    print(f"{num1} + {num2} = {summa}")


show_sum(2, 8)
show_sum(10, 12)

a = 25
b = 17
show_sum(a, b)


# Напишіть функцію, яка приймає два числа як параметри та
# відображає всі числа між ними.

def show_range(start, end):
    for num in range(start, end+1):  # кінець включно
        print(num, end=' ')  # числа через пропуск

    print()  # в кінці перехід на новий рядок


show_range(1, 10)
show_range(100, 105)

end = 20
show_range(1, end)
show_range(1, end-5)

# Напишіть функцію, яка відображає горизонтальну або
# вертикальну лінію. Функція має приймати 3 параметри:
# довжину лінії, символ для заповнення та логічну змінну:
#  Якщо вона рівна True, то лінія горизонтальна
#  Якщо False, то лінія вертикальна

def draw_line(length, symbol, is_horizontal):
    # горизонтальна лінія
    if is_horizontal:
        print(symbol*length)
    else:
        # вертикальна
        for i in range(length):
            print(symbol)


draw_line(5, '-', True)
draw_line(3, '*', False)


# функція яка рахує суму чисел

def get_sum(a, b):
    res = a + b

    # повертає результат
    return res


# text = input('Введіть текст')
# res = min(1, 2)

summa = get_sum(2, 7)
print(summa)
