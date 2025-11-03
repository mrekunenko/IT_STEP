# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

start = min(num1, num2)
end = max(num1, num2)

suma = 0
for i in range(start, end + 1):
    suma += i

print(f"Сума чисел від {start} до {end}: {suma}")


# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

suma = 0
for i in range(1, 101):
    if i % 2 == 0:  # Перевіряємо, чи число парне
        suma += i

print(f"Сума всіх парних чисел від 1 до 100: {suma}")


# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

# Отримуємо рядок від користувача
text = input("Введіть рядок: ")

# Виводимо кожну літеру на окремому рядку
for litera in text:
    print(litera)


# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]

even_numbers = []
for num in numbers:
    if num % 2 == 0:        # перевіряємо, чи число парне
        even_numbers.append(num)

print("Початковий список:", numbers)
print("Парні числа:", even_numbers)


# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

def only_capital(words):
    new_list = []
    for item in words:
        if len(item) > 0 and item[0].isupper():
            new_list.append(item)
    return new_list

# вводимо рядки
user_text = input("Введіть слова через кому: ")

# перетворюємо на список
words = [x.strip() for x in user_text.split(",")]

# виводимо результат
result = only_capital(words)
print("Слова з великої літери:", result)


# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

# Функція повертає рядки, які містять слово "Python"
def filter_python(lines):
    result = []
    for item in lines:
        if "Python" in item:
            result.append(item)
    return result

# вводимо рядки від користувача
user_text = input("Введіть рядки через кому: ")

# формуємо список рядків
lines = [x.strip() for x in user_text.split(",")]

# отримуємо результат
filtered = filter_python(lines)

print("Рядки, що містять 'Python':", filtered)


# Частина 2: Об'єктно-орієнтоване програмування (ООП)
# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.

from datetime import datetime

class WebPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date_published = datetime.now().strftime("%d.%m.%Y %H:%M")

    def display_details(self):
        print("\n" + "=" * 50)
        print("Заголовок:", self.title)
        print("Дата публікації:", self.date_published)
        print("Вміст:")
        print(self.content)
        print("=" * 50)


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):
        # проста перевірка на дубль заголовка (не обов'язково)
        for p in self.pages:
            if p.title == title:
                print("Сторінка з таким заголовком вже існує.")
                return
        self.pages.append(WebPage(title, content))
        print("Сторінку додано.")

    def remove_page(self, title):
        for i, p in enumerate(self.pages):
            if p.title == title:
                del self.pages[i]
                print("Сторінку видалено.")
                return
        print("Сторінку не знайдено.")

    def display_info(self):
        print("\n" + "*" * 50)
        print("Назва сайту:", self.name)
        print("URL:", self.url)
        print("Кількість сторінок:", len(self.pages))
        print("*" * 50)

        if not self.pages:
            print("\nСторінок поки немає")
        else:
            print("\nСторінки на сайті:")
            for i, p in enumerate(self.pages, start=1):
                print(f"{i}. {p.title} ({p.date_published})")


def _input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Поле не може бути порожнім.")


def main():
    site = None
    print("Симулятор вебсайту")
    print("=" * 50)

    while True:
        print("\nМеню:")
        print("1 - Створити сайт")
        print("2 - Додати сторінку")
        print("3 - Видалити сторінку")
        print("4 - Показати інформацію про сайт")
        print("5 - Показати деталі сторінки")
        print("0 - Вийти")

        choice = input("\nВаш вибір: ").strip()

        if choice == "1":
            name = _input_nonempty("Назва сайту: ")
            url = _input_nonempty("URL: ")
            site = WebSite(name, url)
            print("Сайт створено.")

        elif choice == "2":
            if site is None:
                print("Спочатку створіть сайт.")
            else:
                title = _input_nonempty("Заголовок: ")
                content = _input_nonempty("Вміст: ")
                site.add_page(title, content)

        elif choice == "3":
            if site is None:
                print("Спочатку створіть сайт.")
            elif not site.pages:
                print("Немає сторінок.")
            else:
                title = _input_nonempty("Заголовок сторінки для видалення: ")
                site.remove_page(title)

        elif choice == "4":
            if site is None:
                print("Спочатку створіть сайт.")
            else:
                site.display_info()

        elif choice == "5":
            if site is None:
                print("Спочатку створіть сайт.")
            elif not site.pages:
                print("Немає сторінок.")
            else:
                title = _input_nonempty("Заголовок сторінки: ")
                found = False
                for page in site.pages:
                    if page.title == title:
                        page.display_details()
                        found = True
                        break
                if not found:
                    print("Сторінку не знайдено.")

        elif choice == "0":
            print("Програма завершена.")
            break

        else:
            print("Неправильний вибір.")


if __name__ == "__main__":
    main()
