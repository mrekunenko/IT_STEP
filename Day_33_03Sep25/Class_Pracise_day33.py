# Завдання 1
# Створіть абстрактний клас Character, атрибути
# name – ім’я
# max_hp – максимальний рівень здоров’я
# hp – нинішній рівень здоров’я
# level – рівень персонажа(від 1 до 20)
# intelligence – стат інтелекту
# strength – стат сили
# dexterity – стат спритності
# mana – стат мани
# defense – стат захисту
# Методи:
# attack() – абстрактний метод
# take_damage(damage) – отримує урон, зменшений на
# захист
# level_up() – збільшує рівень
# increase_stat(stat) – збільшує один з статів на 1
# rest() – відпочинок(відновлює hp до максимального)
# heal(heal_hp) – збільшує hp на heal_hp
import abc


class Character(abc.ABC):
    def __init__(self, name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.level = level
        self.intelligence = intelligence
        self.strength = strength
        self.dexterity = dexterity
        self.mana = mana
        self.defense = defense

    @abc.abstractmethod
    def attack(self):
        raise NotImplementedError("This method should be implemented")

    def take_damage(self, damage):
        damage_level = damage - self.defense
        if damage_level > 0:
            print(f"You took damage.")
            self.hp -= damage_level
            print(f"Your current HP: {self.hp}")
        else:
            print(f"You are not damaged")

    def level_up(self):
        self.level += 1
        print("You are leveled up")

    def increase_stat(self, stat):
        if stat == "intelligence":
            self.intelligence += 1
            print(f"You boosted your {stat}")

        elif stat == "strength":
            self.strength += 1
            print(f"You boosted your {stat}")

        elif stat == "dexterity":
            self.dexterity += 1
            print(f"You boosted your {stat}")

        elif stat == "mana":
            self.mana += 1
            print(f"You boosted your {stat}")

        elif stat == "defense":
            self.defense += 1
            print(f"You boosted your {stat}")

        else:
            raise ValueError("Wrong stat")

    def rest(self):
        self.hp = self.max_hp
        print("You use rest")

    def heal(self, heal_hp):
        self.hp += heal_hp

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print("You healed your HP")


# hero1 = Character("John", 100, 80, 3,80, 76, 50, 30, 25)
# hero1.take_damage(10)


# Завдання 2
# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana

class Paladin(Character):
    def __init__(self, name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense):
        # Виклик конструктора батьківського класу
        super().__init__(name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense)

    def attack(self):
        if self.mana >= 5:
            damage = 4 * self.strength
            self.mana -= 5
            print(f"{self.name} атакує! Урон: {damage}, витрачено 5 мани. Незалишилось: {self.mana}")
        else:
            damage = self.strength
            print(f"{self.name} атакує! Недостатньо мани. Урон: {damage}")
        return damage

    def shield(self):
        self.defense += 4 + self.level
        print(f"{self.name} активує щит! Захист збільшено до {self.defense}")

    def unshield(self):
        self.defense -= 4 + self.level
        print(f"{self.name} знімає щит! Захист зменшено до {self.defense}")

    def heal_ally(self, ally):
        heal_power = 5 + 2 * self.level + 0.5 * self.mana
        ally.heal(heal_power)
        print(f"{self.name} лікує союзника {ally.name} на {heal_power} HP")

# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та зменшує mana на 5, якщо недостатньо, то не наносить урону
#  heal_ally(ally) – лікує союзника на 3 + level + 3*intelligence

class Mage(Character):
    def attack(selfself):
        if self.mana >= 3:
            damage = 3 * self.intelligence + 4
            self.mana -= 3
            self.spells_cast += 1
            print(f"{self.name} кастує МАГІЧНИЙ СНАРЯД на {damage} урону! (витрачено 3 мани)")
            print(f"Залишилось мани: {self.mana}")
            return damage
        else:
            # Недостатньо мани - не наносимо урону
            print(f"{self.name} намагається кастувати, але недостатньо мани! (потрібно 3, є {self.mana})")
            print("Атака не вдалася!")
            return 0


