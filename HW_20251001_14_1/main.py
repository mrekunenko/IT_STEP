# Завдання 1
#============================================================================================
# Програма складається з трьох потоків.
# Перший просить в користувача вводити числа, поки не введено порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить роботу, і вже потім запускаються.
# Один рахує суму чисел в списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран
import threading


def get_nums(nums):
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")

        if user_input == "":
            break

        try:
            nums.append(float(user_input))

        except ValueError:
            print("Not a valid number!")


def get_nums_sum(nums, results):
    results["sum"] = sum(nums)


def get_nums_avg(nums, results):
    if nums:
        results["avg"] = sum(nums) / len(nums)

    else:
        results["avg"] = 0


nums_list = []
results = {"sum": 0, "avg": 0}

thread_nums_list = threading.Thread(target=get_nums, args=(nums_list,))

thread_nums_list.start()
thread_nums_list.join()

thread_nums_sum = threading.Thread(target=get_nums_sum, args=(nums_list, results))
thread_nums_avg = threading.Thread(target=get_nums_avg, args=(nums_list, results))

thread_nums_sum.start()
thread_nums_avg.start()

thread_nums_sum.join()
thread_nums_avg.join()

print("Num List:", nums_list)
print(f"Num sum: {results['sum']}. Num avg: {results['avg']}")