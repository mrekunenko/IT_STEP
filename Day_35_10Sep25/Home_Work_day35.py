from typing import Any, List, Optional


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.head)

    def push_end(self, data: Any) -> None:
        """
        Додає елемент у кінець списку.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # type: ignore[union-attr]
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data: Any) -> None:
        """
        Додає елемент на початок списку.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node  # type: ignore[union-attr]
            self.head = new_node

    def pop_end(self) -> Optional[Any]:
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if self.tail is None:
            return None

        data = self.tail.data

        if self.head.next is None:  # type: ignore[union-attr]
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None  # type: ignore[union-attr]

        return data

    def pop_start(self) -> Optional[Any]:
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if self.head is None:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None  # type: ignore[union-attr]

        return data


class Shop:
    """
    Реалізація магазину з трьома чергами до кас.
    Кожна черга — це двозв'язний список.
    """

    def __init__(self):
        # Створюємо три окремі черги
        self.queue1 = DoubleLinkedList()
        self.queue2 = DoubleLinkedList()
        self.queue3 = DoubleLinkedList()

    def _get_queue_by_idx(self, idx: int) -> DoubleLinkedList:
        # Повертає посилання на відповідну чергу
        if idx == 1:
            return self.queue1
        elif idx == 2:
            return self.queue2
        elif idx == 3:
            return self.queue3
        else:
            raise ValueError("Індекс черги має бути 1, 2 або 3.")

    def _queue_to_list(self, q: DoubleLinkedList) -> List[str]:
        # Перетворює двозв'язний список у звичайний список для красивого друку
        result: List[str] = []
        current = q.head
        while current is not None:
            result.append(str(current.data))
            current = current.next
        return result

    def add_buyer(self, name: str, idx: int) -> None:
        """
        Додає покупця у кінець черги з номером idx.
        """
        queue = self._get_queue_by_idx(idx)
        queue.push_end(name)

    def serve_buyer(self, idx: int) -> None:
        """
        Обслуговує першого покупця з черги idx.
        Друкує повідомлення та видаляє покупця з черги.
        Якщо черга стала порожньою після обслуговування — викликає _reorder(idx).
        """
        queue = self._get_queue_by_idx(idx)
        served = queue.pop_start()
        if served is None:
            print(f"Черга {idx} порожня. Нема кого обслуговувати.")
            return

        print(f"Обслуговано покупця: {served} з черги {idx}")

        # Перевіряємо, чи стала черга порожньою:
        if queue.head is None:
            self._reorder(idx)

    def _reorder(self, idx: int) -> None:
        """
        Переформування: з кожної черги (1,2,3) беремо останнього покупця (якщо є)
        і переносимо до кінця черги з номером idx.
        """
        target_queue = self._get_queue_by_idx(idx)

        # Послідовно беремо "хвости" в порядку 1,2,3 (включно з idx — якщо вона порожня, pop_end дасть None)
        for source_idx in (1, 2, 3):
            source_queue = self._get_queue_by_idx(source_idx)
            last_buyer = source_queue.pop_end()
            if last_buyer is not None:
                target_queue.push_end(last_buyer)

    def display_info(self) -> None:
        """
        Друкує стан усіх трьох черг.
        """
        q1 = self._queue_to_list(self.queue1)
        q2 = self._queue_to_list(self.queue2)
        q3 = self._queue_to_list(self.queue3)
        print(f"Черга 1: {q1}")
        print(f"Черга 2: {q2}")
        print(f"Черга 3: {q3}")
