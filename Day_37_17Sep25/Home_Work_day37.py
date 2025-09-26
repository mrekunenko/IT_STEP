# Завдання 1
# Використовуючи стеки, змоделюйте роботу над
# виконанням проекту. Як відомо складні завдання часто
# розбивають на під задачі в процесі роботи, і тільки коли всі
# вони виконані вважається що з основним завданням ви
# впорались.
# Створіть клас Project
# Атрибути:
#  tasks – стек з завданнями, об’єкти класу Task ( початкове
# завдання передається в init)
# Методи:
#  do_task() – видалити останнє завдання з стеку та
# виконати його, якщо для цього потрібно зробити під
# завдання, то добавити їх у стек
# Якщо стек порожній то вивести про це повідомлення
#  is_finished() – True якщо завдань не залишилось
# Клас Task(уже реалізований):
#  do() – виконує завдання(виводить на екран інформацію
# про це) та повертає список з підзавданням для
# успішного виконаня


class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def do(self):
        if self.subtasks:
            print(f"Виконую завдання: {self.name}. Розбиваю на підзавдання")
        else:
            print(f"Завершено завдання: {self.name}")
        return self.subtasks


class Project:
    def __init__(self, initial_task: Task):
        # Стартовий стек із початковим завданням
        self.tasks = [initial_task]

    def is_finished(self) -> bool:
        return len(self.tasks) == 0

    def do(self, task: Task):
        return task.do()

    def do_task(self):
        if self.is_finished():
            print("Стек порожній: немає завдань для виконання.")
            return

        current = self.tasks.pop()
        subtasks = self.do(current)

        # Щоб виконувати підзадачі зліва направо — додаємо їх у стек у зворотному порядку
        if subtasks:
            for sub in reversed(subtasks):
                self.tasks.append(sub)
