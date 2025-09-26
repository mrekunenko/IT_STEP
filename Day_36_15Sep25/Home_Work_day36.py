# Завдання 3
# Створіть дочірні класи від Zone та перевизначте метод
# serve_passenger() щоб він повертав пару: пасажир та True/False
# в залежності від успішності перевірки.
# Перевірки:
#  реєстрація – наявність білету(у багажі)
#  безпека – відсутність небезпечних предметів у багажі:
# ніж, зброя, вибухівка
#  посадка – перевірка не потрібна
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет
#  baggage – список з предметами в багажі

from queue import PriorityQueue, Empty
from itertools import count

class Passenger:
    def __init__(self, name, priority, baggage):
        self.name = name
        self.priority = priority
        # нормалізуємо багаж до нижнього регістру
        self.baggage = [str(item).lower() for item in (baggage or [])]

class Zone:
    _seq_gen = count()  # тай-брейкер для однакових пріоритетів

    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add(self, passenger: Passenger):
        seq = next(self._seq_gen)
        self.passengers.put((passenger.priority, seq, passenger))

    def serve_passenger(self):
        """Повертає (passenger, success). У базі — завжди True."""
        if self.passengers.empty():
            return None, False
        _, _, passenger = self.passengers.get()
        print(f'{passenger.name} пройшов зону {self.name}')
        return passenger, True

# Дочірні класи

class RegistrationZone(Zone):
    def __init__(self):
        super().__init__("реєстрація")

    def serve_passenger(self):
        if self.passengers.empty():
            return None, False
        _, _, passenger = self.passengers.get()
        has_ticket = "ticket" in passenger.baggage
        if has_ticket:
            print(f'{passenger.name} пройшов реєстрацію')
            return passenger, True
        else:
            print(f'{passenger.name} не пройшов реєстрацію (немає білету)')
            return passenger, False

class SecurityZone(Zone):
    # множина + нижній регістр
    DANGEROUS_ITEMS = {"knife", "gun", "explosives", "вибухівка", "ніж", "зброя"}

    def __init__(self):
        super().__init__("контроль безпеки")

    def serve_passenger(self):
        if self.passengers.empty():
            return None, False
        _, _, passenger = self.passengers.get()
        found = sorted(set(passenger.baggage).intersection(self.DANGEROUS_ITEMS))
        if found:
            print(f'{passenger.name} не пройшов контроль безпеки (знайдено: {found})')
            return passenger, False
        else:
            print(f'{passenger.name} пройшов контроль безпеки')
            return passenger, True

class BoardingZone(Zone):
    def __init__(self):
        super().__init__("посадка")

    def serve_passenger(self):
        if self.passengers.empty():
            return None, False
        _, _, passenger = self.passengers.get()
        print(f'{passenger.name} пройшов посадку')
        return passenger, True

class Airport:
    def __init__(self):
        self.zones = {
            "register": RegistrationZone(),
            "security_control": SecurityZone(),
            "boarding": BoardingZone()
        }
        self.stats = {
            "registered": 0,
            "security_passed": 0,
            "boarded": 0,
            "registration_failed": 0,
            "security_failed": 0
        }

    def add(self, passenger: Passenger):
        self.zones["register"].add(passenger)

    def serve_registration(self):
        passenger, success = self.zones['register'].serve_passenger() if not self.zones['register'].passengers.empty() else (None, False)
        if passenger is None:
            return
        if success:
            self.zones['security_control'].add(passenger)
            self.stats["registered"] += 1
        else:
            self.stats["registration_failed"] += 1
            print(f'{passenger.name} відмовлено в посадці (не пройшов реєстрацію)')

    def serve_security_control(self):
        passenger, success = self.zones['security_control'].serve_passenger() if not self.zones['security_control'].passengers.empty() else (None, False)
        if passenger is None:
            return
        if success:
            self.zones['boarding'].add(passenger)
            self.stats["security_passed"] += 1
        else:
            self.stats["security_failed"] += 1
            print(f'{passenger.name} відмовлено в посадці (не пройшов контроль безпеки)')

    def serve_boarding(self):
        passenger, success = self.zones['boarding'].serve_passenger() if not self.zones['boarding'].passengers.empty() else (None, False)
        if passenger is None:
            return
        if success:
            self.stats["boarded"] += 1
            print(f'{passenger.name} сів на літак')

    def show_statistics(self):
        print("\n=== СТАТИСТИКА ===")
        print(f"Пройшли реєстрацію: {self.stats['registered']}")
        print(f"Пройшли контроль безпеки: {self.stats['security_passed']}")
        print(f"Сіли на літак: {self.stats['boarded']}")
        print(f"Не пройшли реєстрацію: {self.stats['registration_failed']}")
        print(f"Не пройшли контроль безпеки: {self.stats['security_failed']}")
