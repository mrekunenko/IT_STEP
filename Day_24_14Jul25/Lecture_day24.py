# Є словник, де ключ — ім’я учня, а значення — множина гуртків,
# які він відвідує.
# Реалізуйте функціонал:
# 1 -- додати нового учня
# 2 -- додати новий гурток для учня
# 3 -- видалити гурток для учня
# 4 -- показати учнів які відвідують певний гурток(и)
# 5 -- для двох учнів показати гуртки які вони відвідують разом
# 6 -- вивести всю інформацію.
# 7 -- вивести усі згадані гуртки

students_clubs = {
    "Олег": {"Футбол", "Шахи", "Робототехніка"},
    "Марія": {"Шахи", "Театр"},
    "Іван": {"Футбол", "Програмування", "Робототехніка"},
    "Софія": {"Малювання", "Театр"},
    "Андрій": {"Програмування", "Шахи"},
    "Катерина": {"Футбол", "Малювання"},
}


def get_student():
    """
    Отримати ім'я студента від користувача
    """
    while True:
        student = input("Введіть ім'я студента: ").strip()
        student = student.capitalize()  # зробити першу літеру великою

        if len(student) == 0:
            print('не може бути порожнім')
            continue

        if not student.isalpha():
            print("мають бути лише літери")
            continue

        return student


def get_club():
    """
    Отримати назву гуртка від користувача
    """
    while True:
        club = input("Введіть назву гуртка: ").strip()
        club = club.capitalize()  # зробити першу літеру великою

        if not club:
            print('не може бути порожнім')
            continue

        return club


def add_new_student(students_clubs):
    student = get_student()

    if student in students_clubs:
        print('такий студент вже є')
        return

    students_clubs[student] = set()


def show_info(students_clubs):
    print("Студенти та їхні гуртки")

    for student, clubs in students_clubs.items():
        print(f'\t{student}')
        print('\tГуртки:')

        if clubs:  # якщо не порожній
            for club in clubs:
                print(f"\t\t{club}")
        else:
            print("\t\tНемає")

        print()


def add_new_club(students_clubs):
    student = get_student()

    if student not in students_clubs:
        print("такого студента немає")
        return

    club = get_club()

    if club in students_clubs[student]:
        print('студент уже відвідує цей гурток')
        return

    students_clubs[student].add(club)


def remove_club(students_clubs):
    student = get_student()

    if student not in students_clubs:
        print("такого студента немає")
        return

    club = get_club()

    if club not in students_clubs[student]:
        print('студент не відвідує цей гурток')
        return

    students_clubs[student].remove(club)


def attend_club(students_clubs):
    club = get_club()
    students = []

    for student, clubs in students_clubs.items():
        if club in clubs:
            students.append(student)

    if students:
        for student in students:
            print(f"\t{student}")
    else:
        print(f"Ніхто не відвідує гурток {club}")


def attend_clubs(students_clubs):
    target_clubs = set()
    while True:
        club = get_club()
        target_clubs.add(club)

        choice = input('чи закінчили вводити гуртки?(так/ні)').strip().lower()
        if choice == 'так':
            break

    students = []

    for student, clubs in students_clubs.items():
        if clubs & target_clubs == target_clubs:
            students.append(student)

    if students:
        for student in students:
            print(f"\t{student}")
    else:
        print(f"Ніхто не відвідує ці гуртки {target_clubs}")


def show_common_clubs(students_clubs):
    # student1 = get_student()
    # student2 = get_student()
    #
    # clubs1 = students_clubs[student1]
    # clubs2 = students_clubs[student2]
    #
    # common_clubs = clubs1 & clubs2
    #
    # if common_clubs:
    #     for club in common_clubs:
    #         print(f'\t{club}')
    # else:
    #     print('немає спільних гуртків')

    students = set()
    while True:
        student = get_student()
        students.add(student)

        choice = input('чи закінчили вводити імена?(так/ні)').strip().lower()
        if choice == 'так':
            break

    student = students.pop()
    common_clubs = students_clubs[student]

    for student in students:
        clubs = students_clubs[student]
        common_clubs = common_clubs & clubs

    if common_clubs:
        for club in common_clubs:
            print(f'\t{club}')
    else:
        print('немає спільних гуртків')


def show_all_clubs(students_clubs):
    all_clubs = set()

    for clubs in students_clubs.values():
        all_clubs = all_clubs | clubs  # union

    if all_clubs:
        for club in all_clubs:
            print(f'\t{club}')
    else:
        print('немає інформації про гуртки')


def main():
    """
    Головна функція яка запускає програму.
    """

    print("Меню")
    print("1 -- додати нового учня")
    print("2 -- додати новий гурток для учня")
    print("3 -- видалити гурток для учня")
    print("4 -- показати учнів які відвідують певний гурток(и) усі")
    print("5 -- для двох учнів показати гуртки які вони відвідують разом")
    print("6 -- вивести всю інформацію.")
    print("7 -- вивести усі згадані гуртки")
    print("8 -- вихід")

    while True:
        print()
        choice = int(input("Введіть номер команди: "))

        if choice == 1:
            add_new_student(students_clubs)

        elif choice == 2:
            add_new_club(students_clubs)

        elif choice == 3:
            remove_club(students_clubs)

        elif choice == 4:
            attend_clubs(students_clubs)

        elif choice == 5:
            show_common_clubs(students_clubs)

        elif choice == 6:
            show_info(students_clubs)

        elif choice == 7:
            show_all_clubs(students_clubs)

        elif choice == 8:
            break

        else:
            print('Невідома команда')


if __name__ == '__main__':
    main()
