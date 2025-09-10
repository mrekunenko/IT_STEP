from typing import List


class Passenger:
    """
    Клас пасажира з ім'ям та пунктом призначення.
    """
    def __init__(self, name: str, destination: str) -> None:
        self.name = str(name)
        self.destination = str(destination)

    def __repr__(self) -> str:
        return f"Passenger(name={self.name!r}, destination={self.destination!r})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Passenger):
            return False
        return (self.name == other.name) and (self.destination == other.destination)


class Transport:
    """
    Транспорт із заданою швидкістю.
    """
    def __init__(self, speed: float) -> None:
        self.speed = float(speed)

    def move(self, destination: str, distance: float) -> float:
        """
        Рухається до місця призначення.

        Повертає час у годинах та ВИВОДИТЬ (print) інформацію.
        """
        hours = float(distance) / self.speed
        print(f"Їдемо до {destination}. Відстань {distance} км зі швидкістю {self.speed} км/год. Час у дорозі: {hours:.2f} год.")
        return hours


class Bus(Transport):
    """
    Автобус із пасажирами та обмеженою місткістю.
    """
    def __init__(self, speed: float, capacity: int) -> None:
        super().__init__(speed)
        self.capacity = int(capacity)
        self.passengers: List[Passenger] = []

    def board_passenger(self, passenger: Passenger) -> bool:
        """
        Додає пасажира, якщо є місце. Повертає True/False.
        """
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        else:
            return False

    def move(self, destination: str, distance: float) -> tuple[int, float]:
        """
        Висаджує усіх пасажирів, які хочуть вийти у 'destination'.
        Виводить їхню кількість. Потім викликає Transport.move.
        Повертає (кількість_висаджених, час_у_годинах).
        """
        to_drop = [p for p in self.passengers if p.destination == destination]
        dropped = len(to_drop)
        # Видаляємо цих пасажирів зі списку
        self.passengers = [p for p in self.passengers if p.destination != destination]
        print(f"Висаджено пасажирів у {destination}: {dropped}")
        hours = super().move(destination, distance)
        return dropped, hours
