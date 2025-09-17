# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
#
# class DoubleLinkedList:
#     """
#     Клас двозв'язного списку.
#     """
#
#     def __init__(self):
#         """
#         Ініціалізація порожнього списку.
#         """
#         self.head = None
#         self.tail = None
#
#     def __str__(self):
#         return str(self.head)
#
#     def push_end(self, data):
#         """
#         Додає елемент у кінець списку.
#         :param data: Дані для додавання
#         """
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#
#     def push_start(self, data):
#         """
#         Додає елемент на початок списку.
#         :param data: Дані для додавання
#         """
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#
#     def pop_end(self):
#         """
#         Видаляє останній елемент зі списку.
#         :return: Дані видаленого елемента або None, якщо список порожній
#         """
#         if not self.tail:
#             return None
#
#         data = self.tail.data
#
#         if self.head.next is None:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#
#         return data
#
#     def pop_start(self):
#         """
#         Видаляє перший елемент зі списку.
#         :return: Дані видаленого елемента або None, якщо список порожній
#         """
#
#         if not self.head:
#             return None
#
#         data = self.head.data
#
#         if self.head.next is None:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#         return data
#
# #очереди
#
# class Queue:
#     def __init__(self):
#         self.queue = DoubleLinkedList()
#         self.item_count = 0
#
#     def push(self, item): #append\enqueue\put
#         self.queue.push_end(item)
#         self.item_count += 1
#
#     def pop(self): #get\dequeue
#         item = self.queue.pop_start()
#         self.item_count -= 1
#
#         return  item
#
#     def __len__(self):
#         return  self.item_count
#
#     def __str__(self):
#         return  str(self.queue)
#
# queue = Queue()
#
# #dobavit elementi
#
# queue.push('Mary')
# queue.push('John')
# queue.push('Mark')
# queue.push('Anna')
#
# print(queue)
#
# #dostat element
#
# person = queue.pop()
# print(person)
# print(queue)
from multiprocessing.resource_tracker import register
#тоже cамое через  встроенный класс

# from queue import  Queue
#
# queue = Queue()
#
# #dobavit elementi
#
# queue.put('Mary')
# queue.put('John')
# queue.put('Mark')
# queue.put('Anna')
#
# print(queue)
#
# #dostat element
#
# person = queue.get()
# print(person)
# print(queue)

# from  queue import   Queue
# import datetime
# import time
#
# class Message:
#     def __init__(self, text):
#         self.text = text
#         self.time = datetime.datetime.now().time() #теперішній час
#
#     def __str__(self):
#         return  f'[{self.time.strftime("%H:%M:%S")}] {self.text}'
#
# #простой мессенджер
# class Messanger:
#     def __init__(self):
#         self.messages  = Queue()
#
#     def add_message(self, text):
#         message = Message(text)
#         self.messages.put(message)
#
#         print('повідомлення доданно')
#
#     def read_message(self):
#         if self.messages.empty():
#             print('No messages')
#             return
#
#         message = self.messages.get()
#         print(message)
#
#         return message
#
#
#
# messagner = Messanger()
#
# messagner.add_message("Hello")
# messagner.add_message("How are you?")
# messagner.add_message("Fine")
# messagner.read_message()
# messagner.add_message("Thx")
#
# messagner.read_message()
# messagner.read_message()
# messagner.read_message()
# messagner.read_message()
# messagner.read_message()

#черга з пріорітетом
# osnovna stkrytyra dannih -- kypa
#
# from queue import  PriorityQueue
#
# queue = PriorityQueue()
#
# #dobavit element s prioritetom
# #queue.put((priority, item))
# queue.put((3, "John")) #dobavit John s prioritetom 3
# queue.put((2, "Angelina"))
# queue.put((1, "Anna"))
# queue.put((1, "Mark"))
# queue.put((2, "Mary"))
# queue.put((3, "Mike"))
# # в межах одного пріорітету елементи сзеьрігаються у відсортованому вигляді по алфафіту
#
# item =  queue.get()
# print(item)
# item =  queue.get()
# print(item)
# item =  queue.get()
# print(item)
# item =  queue.get()
# print(item)
# item =  queue.get()
# print(item)
# item =  queue.get()
# print(item)

# Завдання 1
# Посилання на код
# Використовуючи чергу створіть клас FastFoodQueue для організації роботи черг у фасфуді. Є 4 каси, новий клієнт стає в ту, де найменше людей. Коли клієнт зробив замовлення, його добавляють в чергу на отримання. Має зберігатися час, коли людина зробила замовлення, та коли отримала замовлення. Інформація про час обслуговування має зберігатись у окремому списку
# Атрибути:
#  queues – список з 4-ма чергами до кас
#  order_queue – черга клієнтів на отримання замовлення
#  service_duration_history – список з часом обслуговування клієнтів
# Методи:
#  add(client) – додає клієнта в найкоротшу чергу
#  serve(idx) – обслуговуємо клієнта з черги за індексом. Треба додати клієнта в order_queue разом з часом коли зроблено замовлення
#  make_order() – видає готове замовлення клієнту та обраховує скільки часу очікував клієнт. Це число треба добавити в service_duration_history
# Практичне завдання
#  show_statistics() – виводить мінімальний, максимальний та середній час обслуговування клієнтів
# from queue import Queue
# import time
#
# class Client:
#     def __init__(self, name):
#         self.name = name
#         self.time = time.time()
#
# # TASK 1
# class FastFoodQueue:
#     def __init__(self):
#         self.queues = [Queue(), Queue(), Queue(), Queue() ]
#         self.order_queue = Queue()
#         self.service_duration_history = []
#
#     def add(self,client_name):
#         min_queue_len = min(self.queues, key=lambda item: item.qsize())
#         min_queue_len.put(client_name)
#
#     def serve(self, idx):
#         if  self.queues[idx].empty():
#             print('This queue is empty')
#             return
#
#         client_name = self.queues[idx].get()
#         client = Client(client_name)
#         print(f'{client_name}- had served')
#
#         self.order_queue.put(client)
#
#
#
#     def make_order(self):
#         client = self.order_queue.get()
#         print(f'{client.name} -- received  order')
#
#
#         current_time = time.time()
#         order_time  = current_time - client.time
#         self.service_duration_history.append(order_time)
#
#     def show_statistics(self):
#         min_time = min(self.service_duration_history)
#         max_time = max(self.service_duration_history)
#         avg_time = sum(self.service_duration_history) / len(self.service_duration_history)
#
#         print(f'min time = {min_time}\nMax time = {max_time}\naverage time = {avg_time} ')
#
# # Тестування
# fast_food = FastFoodQueue()
# fast_food.add("Олег")
# fast_food.add("Анна")
# fast_food.add("Марія")
# fast_food.add("Сергій")
#
# fast_food.serve(0)
# fast_food.serve(1)
#
# time.sleep(2)
# fast_food.make_order()
# time.sleep(3)
# fast_food.make_order()
#
# fast_food.show_statistics()


# Завдання 2
# Використовуючи черги з пріоритетом створіть програму для симуляції роботи аеропорту. Кожен пасажир має пройти через 3 етапи: реєстрація, контроль безпеки, посадка. Відповідно аеропорт складається з 3-ох зон, кожна з яких має свою чергу. Коли Пасажир пройшов одну зону, то переходить в наступну.
# Пасажири з вищим пріоритетом обслуговуються першими
# Клас Zone – зона
# Атрибути:
#  name – назва(реєстрація, контроль безпеки або посадка)
#  passengers – черга пасажирів
# Методи:
#  add(passenger) – додає пацієнта в чергу з пріоритетом
#  serve_passenger() – обслуговуємо наступного пасажира та повертає його
# Клас Airport – аеропорт
# Атрибути:
#  zones – словник із зонами, ключем є назва зони
#  passengers – список пасажирів, які успішно пройшли 3 зони
# Методи:
#  add(passenger) – додає пасажира в чергу на реєстрацію
#  serve_registration() – обслуговує клієнта з черги реєстрації та переводить на котроль безпеки
#  serve_security_control() – обслуговує клієнта з черги контролю безпеки та переводить на посадку
#  serve_boarding() – обслуговує клієнта з черги посадки та переводить в passengers
#  show_statistics() – вивести кількість пасажирів у кожній зоні та скільки успішно все пройшли
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет
# TASK 2
from  queue import  PriorityQueue

class Passenger:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def  add(self, passenger: Passenger):
        priority = passenger.priority
        self.passengers.put((priority, passenger))

    def serve_passenger(self):
        priority, passenger = self.passengers.get()
        print(f'{passenger.name} пройшов зону {self.name}')

        return  passenger


class Airport:
    def __init__(self):
        self.zones = {"register": Zone("register"), "security_control": Zone("_security_control"), "boarding": Zone("boarding") }

    def add(self, passenger: Passenger):
        self.zones["register"].add(passenger)

    def serve_registration(self):
        passanger = self.zones['register'].serve_passenger()
        self.zones['security_control'].add(passanger)

    def serve_security_control(self):
        passanger = self.zones['security_control'].serve_passenger()
        self.zones['boarding'].add(passanger)

    def serve_boarding(self):
        passenger = self.zones['boarding'].serve_passenger()
        print(f'{passenger.name} сів на літак')




# Тестування
airport = Airport()
passengers = [
    Passenger("Олег", 3),
    Passenger("Анна", 1),
    Passenger("Марія", 4),
    Passenger("Сергій", 2)
]


for p in passengers:
    airport.add(p)

airport.serve_registration()
airport.serve_registration()
airport.serve_security_control()
airport.serve_boarding()

airport.show_statistics()









# Завдання 3
# Створіть дочірні класи від Zone та перевизначте метод serve_passenger() щоб він повертав пару: пасажир та True/False в залежності від успішності перевірки.
# Перевірки:
#  реєстрація – наявність білету(у багажі)
#  безпека – відсутність небезпечних предметів у багажі: ніж, зброя, вибухівка
#  посадка – перевірка не потрібна
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет
#  baggage – список з предметами в багажі