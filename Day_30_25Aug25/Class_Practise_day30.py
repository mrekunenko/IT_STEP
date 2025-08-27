# # Завдання 1
# # Створіть клас Проект з атрибутами:
# #  назва
# #  виділений кошторис
# #  загальні витрати
# #  чи завершений(за замовчуванням False)
# #  час виконання(за замовчуванням 0 місяців)
# #  список необхідних задач
# # Додайте методи:
# #  вивід інформації: назва, час виконання, необхідні
# # задачі
# #  добавити нову задачу
# #  розбити задачу на під-задачі: передається назва задачі
# # та список під-задач
# #  виконати задачу, передається назва, час та ціна
# # виконання
# #  поповнення кошторису
#
#
# # опис класу
# # (шаблон який описує всі проекти)
# class Project:
#     def __init__(self, name: str, budget: int, tasks: list):
#         self.name = name
#         self.budget = budget
#         self.tasks = tasks
#
#         self.expenses = 0
#         self.is_finished = False
#         self.time = 0
#
#     def show_info(self):
#         print()
#         print(f"Інформація по проекту {self.name}")
#         print(f'\t Бюджет -- {self.budget}грн')
#         print(f"\t Використано -- {self.expenses}/{self.budget}")
#         print(f"\t Час виконання -- {self.time} місяців")
#
#         if self.is_finished:
#             print(f'\t Статус -- Завершений')
#         else:
#             print(f'\t Статус -- Незавершений')
#
#         print('\t Список задач:')
#         for task in self.tasks:
#             print(f"\t\t {task}")
#
#     def add_task(self, new_task):
#         self.tasks.append(new_task)
#         print(f"Додано нове завдання {new_task}")
#
#     def create_subtasks(self, old_task, subtasks):
#         # чи є стара задачі в списку
#         if old_task not in self.tasks:
#             print(f"Такої задачі немає в списку")
#             return
#
#         # old_task є в списку
#         self.tasks.remove(old_task)
#         self.tasks.extend(subtasks)  # добавити всі елементи з subtasks в список self.tasks
#
#         # # спосіб де багато відступів
#         # if old_task in self.tasks:
#         #     # old_task є в списку
#         #     self.tasks.remove(old_task)
#         #     self.tasks.extend(subtasks)  # добавити всі елементи з subtasks в список self.tasks
#         # else:
#         #     print(f"Такої задачі немає в списку")
#
#     def do_task(self, task, price, time):
#         if task not in self.tasks:
#             print(f"Такої задачі немає в списку")
#             return
#
#         if price > (self.budget - self.expenses):
#             print('Не вистачає коштів')
#             return
#
#         # все добре, робимо задачу
#         self.tasks.remove(task)
#         self.expenses += price
#         self.time += time
#
#         self.is_finished = len(self.tasks) == 0
#
#     def deposit(self, price):
#         self.budget += price
#
#
#
#
# # створення конкретного проекту
# project1 = Project('Making Film', 10000, ['write plot', 'find actors'])
# project2 = Project('Create Site', 5000, ['create name', 'create database'])
#
# # print(project1.tasks)
# # print(project1.is_finished)
#
# project1.show_info()
#
# project1.add_task("find location")
# project1.show_info()
# print(project1.tasks)
#
#
# project1.create_subtasks('talk with producer', [])
#
# project1.create_subtasks("find actors",
#                          ['talk with actor1', 'talk with actor2'])
# project1.show_info()
#
# project1.do_task('talk with actor1', 1000, 0.5)
# project1.show_info()
#
# project1.do_task('write plot', 20000, 3.5)
#
# project1.deposit(50000)
# project1.do_task('write plot', 20000, 3.5)
# project1.show_info()


# Завдання 2: Клас Телефон
class Phone:
    def __init__(self, max_memory, used_memory):
        self.max_memory = max_memory
        self.used_memory = used_memory
        self.is_poweron = False
        self.apps = {'Youtube': 5, 'Google': 20}

    def show_memory_used(self):
        print(f' used memory {self.used_memory} Mb')
        print(f'Max memory')


