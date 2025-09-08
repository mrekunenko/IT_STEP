# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5

from abc import ABC, abstractmethod


from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name: str, satiety: int = 50, energy: int = 50):
        self.name = str(name)
        self.satiety = self._clamp(satiety)
        self.energy = self._clamp(energy)

    @staticmethod
    def _clamp(v: int) -> int:
        return max(0, min(100, int(v)))

    def sleep(self) -> None:
        """Заряджає енергію до 100."""
        self.energy = 100

    def eat(self, food_amount: int) -> None:
        """+сатість на food_amount (обмежуємо до 100)."""
        if food_amount < 0:
            raise ValueError("food_amount має бути ≥ 0")
        self.satiety = self._clamp(self.satiety + int(food_amount))

    @abstractmethod
    def play(self, activity_level: int) -> None:
        """Абстрактний метод гри."""
        ...

    def make_sound(self) -> None:
        """Базова реалізація — нічого не робить."""
        pass

    def status(self) -> str:
        return f"{self.name}: satiety={self.satiety}, energy={self.energy}"


class Cat(Pet):
    def play(self, activity_level: int) -> None:
        """Якщо satiety > 60: energy -= 2*activity_level, satiety -= activity_level."""
        activity_level = int(activity_level)
        if self.satiety > 60:
            e_drop = 2 * activity_level
            s_drop = activity_level
            self.energy = self._clamp(self.energy - e_drop)
            self.satiety = self._clamp(self.satiety - s_drop)
            print(f"{self.name} грає: -{e_drop} енергії, -{s_drop} ситості.")
        else:
            print(f"{self.name} занадто голодний(а) для ігор.")

    def make_sound(self) -> None:
        print("Мяу")

    def catch_mouse(self) -> None:
        """Ловить мишу, якщо energy > 30; якщо satiety > 40 — грається, інакше — їсть."""
        if self.energy > 30:
            print(f"{self.name} упіймав(ла) мишу!")
            if self.satiety > 40:
                print(f"{self.name} грається з мишею.")
            else:
                print(f"{self.name} з'їдає мишу.")
        else:
            print(f"{self.name} занадто втомлений(а), щоб ловити мишей.")


class Dog(Pet):
    def play(self, activity_level: int) -> None:
        """Якщо satiety > 15: energy -= a//2, satiety -= a//2."""
        activity_level = int(activity_level)
        if self.satiety > 15:
            drop = activity_level // 2
            self.energy = self._clamp(self.energy - drop)
            self.satiety = self._clamp(self.satiety - drop)
            print(f"{self.name} грає: -{drop} енергії, -{drop} ситості.")
        else:
            print(f"{self.name} занадто голодний(а) для ігор.")

    def make_sound(self) -> None:
        print("Гав")

    def fetch_ball(self) -> None:
        """Ловить м'яч, якщо satiety > 10; energy -= 5."""
        if self.satiety > 10:
            print(f"{self.name} приніс(ла) м'яч!")
            self.energy = self._clamp(self.energy - 5)
        else:
            print(f"{self.name} занадто голодний(а), щоб бігати за м'ячем.")


# --- ДЕМО ---
if __name__ == "__main__":
    cat = Cat("Лелік", satiety=70, energy=80)
    dog = Dog("Барс", satiety=20, energy=60)

    print(cat.status())
    cat.play(10)          # -20 енергії, -10 ситості
    cat.catch_mouse()     # енергії > 30 -> ловить; ситість > 40 -> грається
    cat.make_sound()
    print(cat.status(), "\n")

    print(dog.status())
    dog.play(9)           # -4 енергії, -4 ситості
    dog.fetch_ball()      # -5 енергії (бо ситість > 10)
    dog.make_sound()
    print(dog.status(), "\n")

    cat.eat(40)           # ситість до 100
    cat.sleep()           # енергія до 100
    print("Після їжі та сну:", cat.status())
