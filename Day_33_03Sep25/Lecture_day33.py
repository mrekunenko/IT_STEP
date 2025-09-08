# Наслідування(успадкування) класів

# батьківський клас
# В ньому розписані спільні методи/атрибути для інших класів
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f'{self.name} спить')

    def grow(self):
        self.age += 1

    def make_sound(self):
        print('Якийсь звук')

    def __str__(self):
        return f"Name: {self.name}, age: {self.age} years"

    def display_info(self):
        print(f'Name -- {self.name}')
        print(f'Age -- {self.age} years')


# Дочірній клас -- клас який отрмує всі методи з батьківського
# плюс власні методи
# class ДочірнійКлас(БатківськийКлас)
class Cat(Pet):
    def __init__(self, name, age, weight):
        # виклик батьківського init
        super().__init__(name, age)

        # нові атрибути
        self.weight = weight


    # перевантажений метод(він замінює однойменний з класу Pet)
    def make_sound(self):  # метод з такою ж назвою як в Pet
        print('Мяу')

    # додати до батьківського методу додатковий функціонал
    # display_info додатково показував що це кіт
    def display_info(self):
        print('Cat')  # додатковий функціонал

        # запустити батківський метод(Pet.display_info)
        super().display_info()
        print(f'Weight -- {self.weight} kg')



cat = Cat('Том', 2, 3.5)
cat.sleep()
print(cat)
cat.grow()
print(cat)
cat.make_sound()

cat.display_info()

print(Cat.__mro__)