# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть

from datetime import datetime, time

class Message:
    def __init__(self, user: str, text: str):
        self.user = user
        self.text = text
        self.time = datetime.now()

    def __str__(self):
        return f'Time: {self.time.strtime('%H:%M')}, user: {self.user}, message: "{self.text}"'

    def __len__(self):
        return len(self.text)

    def __gt__(self, other):
        if isinstance(other, Message):
            return self.time > other.time
        else:
            raise TypeError(f'Unsupported operation')

mess1 = Message('Vlad', "Hellp")
print(mess1)
print(len(mess1))

