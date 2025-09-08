# # Наслідування(успадкування) класів
#
# #батьківскьй класс
# #в ньому розписані спільни методи та атрабиту  для інших класив
#
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(f'{self.name} sleep')
#
#     def grow(self):
#         self.age += 1
#
#     def __str__(self):
#         return  f'Name: {self.name}, age: {self.age} years'
#
#     def display_info(self):
#         print(f'name -- {self.name}')
#         print(f'age -- {self.age} years')
#
#
# #дочірній класс -- класс який отримує всі методи за батьківського також має свої(subclass)
# #class(батьківскій класс)
# class Cat(Pet):
#     def __init__(self, name, age, weight):
#         #viklik otsovskogo innita
#         super().__init__(name, age)
#
#         self.weight = weight
#
#
#     def make_sound(self):
#         print('MEOW')
#
#     #add to main class + funcional
#     #display_info dodatkovo pokazyvav sho ce kit
#     def display_info(self):
#         print('Cat')
#         #zapystit kod s batikskovogo metoda(Pet.display_info)
#         super().display_info()
#         print(f'weight -- {self.weight}')
#
#
#
#
# cat = Cat("Tom", 2, 3.5)
# cat.sleep()
# print(cat)
# cat.grow()
# print(cat)
# cat.make_sound()
# cat.display_info()
#
# print(Cat.__mro__)


#  Завдання 1
# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я
#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense –  стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp
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
        raise  NotImplementedError('this method should be implemented in subclass')

    def take_damage(self, damage):
        damage_level = damage - self.defense
        if damage_level > 0:
            print(f'You took damage. ')
            self.hp -= damage_level
            print(f'your current hp is {self.hp}')
            if self.hp <= 0:
                print('YOU DEAD! GAME OVER!')

        else:
            print(f'You DID NOT took damage. ')

    def level_up(self):
        self.level += 1
        print("U r lvled up")

    def increase_stat(self,stat):
        if stat == "intelligence":
            self.intelligence += 1
            print(f'You boosted your {stat}')

        if stat == "strength":
            self.strength += 1
            print(f'You boosted your {stat}')

        if stat == "dexterity":
            self.dexterity += 1
            print(f'You boosted your {stat}')

        if stat == "mana":
            self.mana += 1
            print(f'You boosted your {stat}')

        if stat == "defense":
            self.defense += 1
            print(f'You boosted your {stat}')

        else:
            raise ValueError('wrong stat')

    def rest(self):
        self.hp = self.max_hp
        print('You had rest now your HP full')

    def heal(self, heal_hp):
        # if self.hp + heal_hp > self.max_hp:
        #     self.hp = self.max_hp
        # else:
        #     self.hp += heal_hp
        self.hp += heal_hp

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print('You healed your hp')


# hero1 = Character('John',100, 80, 3, 80, 76,50,50,25)
#
# hero1.take_damage(10)
# Завдання 2
# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana
class Paladin(Character):
    def attack(self):
        if  self.mana >= 5:
            self.mana -= 5
            return  self.strength * 4
        else:
            return  self.strength

    def shield(self):
        self.defense += 4
        self.defense += self.level

    def unshield(self):
        self.defense -= 4
        self.defense -= self.level

    def heal_ally(self,ally: Character):
        heal_hp = 5 + (2 * self.level) + (0.5 * self.mana)
        ally.heal(heal_hp)

    def rest(self):
        super().rest()

        self.mana += 10

# paladin1 = Paladin('John',100, 80, 3, 80, 76,50,50,25)
# paladin2 = Paladin('Tom',100, 90, 5, 50, 76,50,20,25)

# paladin1.shield()
# paladin1.take_damage(50)
# paladin2.heal_ally(paladin1)
# print(paladin1.hp)
# print(paladin2.attack())
# print(paladin2.attack())
# print(paladin2.attack())
# print(paladin2.attack())
# print(paladin2.attack())
# print(paladin2.attack())

# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить
# урону
#  heal_ally(ally) – лікує союзника на 3 + level +
# 3*intelligence

class Mage(Character):
    def attack(self):
       if self.mana < 3:
           print('0 damage')
           return  0
       else:
           atk = (3 * self.intelligence) + 4
           self.mana -= 3
           print(f'ви нанесли {atk} damage')
           return  atk

    def fireball(self):
        if self.mana < 5:
            print('0 damage')
            return 0
        else:
            atk = (2 * self.intelligence) + 3
            self.mana -= 5
            print(f'ви нанесли firaball atack {atk} damage ')
            return  atk

    def heal_ally(self, ally: Character):
        heal_hp = (3 + self.level) + (3 * self.intelligence)
        ally.heal(heal_hp)

    def rest(self):
        super().rest()

        self.mana += 10


mage =  Mage('Tom',100, 60, 6, 10, 46,30,10,15)
paladin2 = Paladin('Tom',100, 60, 5, 50, 76,50,20,25)

mage.attack()
mage.fireball()
mage.attack()
mage.fireball()
mage.attack()
mage.fireball()

print(paladin2.hp)
mage.heal_ally(paladin2)
print(paladin2.hp)

print(mage.hp)
paladin2.heal_ally(mage)
print(mage.hp)

# Завдання 4
# Створіть дочірній клас Warrior
# Методи:
#  attack() – наносить 4*strength+3 урону
#  power_strike(enemies) – проходить по списку ворогів: якщо їхній рівень менший за рівень персонажа, то знищує його повністю

class Warrior(Character):
    def attack(self):
        dmg = 4 * self.strength + 3
        print(f"{self.name} strikes: {dmg} dmg")
        return dmg

    def power_strike(self, enemies):
        if enemies is None:
            print(f"{self.name} swings at nothing (no enemies).")
            return []

