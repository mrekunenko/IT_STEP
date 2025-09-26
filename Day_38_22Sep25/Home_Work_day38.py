# Завдання 1
# Використовуючи бінарні дерева, організуйте роботу
# автопарку, де зберігаються автомобілі, відсортовані за
# маркою
# Клас Car
# Атрибути:
#  brand – модель автомобіля
#  model – марка автомобіля
#  year – рік випуску
# Клас CarPark
# Атрибути:
#  cars – дерево з автомобілями
# Методи:
#  add(car) – добавити автомобіль
#  remove(model) – видалити автомобіль
#  search(model) – пошук автомобіля за маркою, якщо є
# то повертає ??книгу?? (мабуть, помилка в умові - має бути "автомобіль")
# інакше None
#  __len__() – кількість автомобілів
#  sell_car(client, model) – продати автомобіль клієнту,
# якщо така марка присутня

from typing import Optional, List


class Car:
    """Клас для представлення автомобіля"""

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand  # марка автомобіля (Toyota, BMW, etc.)
        self.model = model  # модель автомобіля (Camry, X5, etc.)
        self.year = year  # рік випуску

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.year})"


class TreeNode:
    """Вузол бінарного дерева"""

    def __init__(self, brand: str):
        self.brand = brand  # ключ вузла (оригінальний регістр марки)
        self.cars: List[Car] = []  # список автомобілів цієї марки
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class CarPark:
    """Клас для управління автопарком з використанням бінарного дерева"""

    def __init__(self):
        self.cars: Optional[TreeNode] = None  # корінь дерева
        self._size = 0  # кількість автомобілів

    @staticmethod
    def _key(brand: str) -> str:
        """Нормалізація ключа (нечутливо до регістру)"""
        return brand.lower().strip()

    def add(self, new_car: Car) -> None:
        """Додати автомобіль до дерева"""
        if self.cars is None:
            node = TreeNode(new_car.brand)
            node.cars.append(new_car)
            self.cars = node
            self._size += 1
        else:
            self._add_recursive(self.cars, new_car)

    def _add_recursive(self, node: TreeNode, new_car: Car) -> None:
        """Рекурсивне додавання автомобіля"""
        if self._key(new_car.brand) < self._key(node.brand):
            if node.left is None:
                new_node = TreeNode(new_car.brand)
                new_node.cars.append(new_car)
                node.left = new_node
                self._size += 1
            else:
                self._add_recursive(node.left, new_car)
        elif self._key(new_car.brand) > self._key(node.brand):
            if node.right is None:
                new_node = TreeNode(new_car.brand)
                new_node.cars.append(new_car)
                node.right = new_node
                self._size += 1
            else:
                self._add_recursive(node.right, new_car)
        else:
            # Марка вже існує - додаємо до списку
            node.cars.append(new_car)
            self._size += 1

    def _search_node(self, node: Optional[TreeNode], brand: str) -> Optional[TreeNode]:
        """Знайти вузол за маркою"""
        if node is None:
            return None

        if self._key(brand) == self._key(node.brand):
            return node
        elif self._key(brand) < self._key(node.brand):
            return self._search_node(node.left, brand)
        else:
            return self._search_node(node.right, brand)

    def search(self, brand: str) -> Optional[Car]:
        """Пошук автомобіля за маркою, повертає перший знайдений або None"""
        node = self._search_node(self.cars, brand)
        return node.cars[0] if node and node.cars else None

    def remove(self, brand: str) -> Optional[Car]:
        """Видалити один автомобіль за маркою, повертає видалений Car або None"""
        node = self._search_node(self.cars, brand)

        if node and node.cars:
            # Видаляємо перший автомобіль зі списку
            removed_vehicle = node.cars.pop(0)
            self._size -= 1

            # Якщо список спорожнів, видаляємо вузол з дерева
            if not node.cars:
                self.cars = self._remove_empty_node(self.cars, brand)

            return removed_vehicle

        return None

    def _remove_empty_node(self, node: Optional[TreeNode], brand: str) -> Optional[TreeNode]:
        """Видалити порожній вузол з дерева"""
        if node is None:
            return None

        if self._key(brand) < self._key(node.brand):
            node.left = self._remove_empty_node(node.left, brand)
            return node
        elif self._key(brand) > self._key(node.brand):
            node.right = self._remove_empty_node(node.right, brand)
            return node
        else:
            # Знайшли вузол для видалення
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Вузол має два дочірніх вузли
                min_node = self._find_min(node.right)
                node.brand = min_node.brand
                node.cars = min_node.cars[:]  # копіюємо список
                node.right = self._remove_empty_node(node.right, min_node.brand)
                return node

    @staticmethod
    def _find_min(node: TreeNode) -> TreeNode:
        """Знайти мінімальний вузол у піддереві"""
        while node.left is not None:
            node = node.left
        return node

    def sell_car(self, brand: str) -> Optional[Car]:
        """Продати автомобіль, повертає проданий Car або None"""
        sold_vehicle = self.remove(brand)
        return sold_vehicle

    def __len__(self) -> int:
        """Повернути кількість автомобілів"""
        return self._size

    def display_all(self) -> List[Car]:
        """Відобразити всі автомобілі в відсортованому порядку за марками"""
        cars = []
        self._inorder_traversal(self.cars, cars)
        return cars

    def _inorder_traversal(self, node: Optional[TreeNode], cars_list: List[Car]) -> None:
        """Симетричний обхід дерева для отримання відсортованого списку"""
        if node is not None:
            self._inorder_traversal(node.left, cars_list)
            cars_list.extend(node.cars)  # додаємо всі автомобілі з вузла
            self._inorder_traversal(node.right, cars_list)

    def get_cars_by_brand(self, brand: str) -> List[Car]:
        """Отримати всі автомобілі певної марки"""
        node = self._search_node(self.cars, brand)
        return node.cars[:] if node else []  # повертаємо копію списку


