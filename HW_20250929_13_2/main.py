# Завдання 1
#==========================================================================================
# Напишіть програму для збереження даних про музичні групи у вигляді словника,
# де ключ – назва групи, значення – список альбомів.
# Напишіть функціонал:
# додати новий гурт
# додати новий альбом
# зберегти дані через json
# зберегти дані через pickle
# завантажити дані через json
# завантажити дані через pickle
import json
import pickle
import os


class Group:
    def __init__(self, name):
        self.group_name = name
        self.album_list = []

    def add_new_album(self):
        album_title = input("Enter album title: ")

        if album_title in self.album_list:
            print("Album with this title already exists in this group")
            return

        self.album_list.append(album_title)
        print("Album added successfully!")

    def save_data_json(self):
        if os.path.exists("groups.json"):
            with open("groups.json", "r", encoding="utf-8") as file:
                group_list = json.load(file)
        else:
            group_list = {}

        group_list[self.group_name] = self.album_list

        with open("groups.json", "w", encoding="utf-8") as file:
            json.dump(group_list, file, indent=4)
        print("Data saved to groups.json")

    def save_data_pickle(self):
        if os.path.exists("groups.pkl"):
            with open("groups.pkl", "rb") as file:
                group_list = pickle.load(file)
        else:
            group_list = {}

        group_list[self.group_name] = self.album_list

        with open("groups.pkl", "wb") as file:
            pickle.dump(group_list, file)
        print("Data saved to groups.pkl")

    def load_data_json(self):
        if not os.path.exists("groups.json"):
            print("No JSON file found.")
            return

        with open("groups.json", "r", encoding="utf-8") as file:
            group_list = json.load(file)

        self.album_list = group_list[self.group_name]
        print(f"Loaded albums for {self.group_name}: {self.album_list}")

    def load_data_pickle(self):
        if not os.path.exists("groups.pkl"):
            print("No Pickle file found.")
            return

        with open("groups.pkl", "rb") as file:
            group_list = pickle.load(file)

        self.album_list = group_list[self.group_name]
        print(f"Loaded albums for {self.group_name}: {self.album_list}")


groups = {}

while True:
    print("\nChoose service:")
    print("1 - Add new group")
    print("2 - Add new album to group")
    print("3 - Load group data (JSON)")
    print("4 - Load group data (Pickle)")
    print("5 - Save all groups (JSON)")
    print("6 - Save all groups (Pickle)")
    print("7 - Exit")

    try:
        user_choice = int(input("Your choice: "))

    except ValueError:
        print("Please enter a number!")
        continue

    if user_choice == 1:
        group_name = input("Enter group name: ")

        if group_name in groups:
            print("Group already exists in memory")

        else:
            groups[group_name] = Group(group_name)
            print(f"Group '{group_name}' created.")

    elif user_choice == 2:
        group_name = input("Enter group name: ")

        if group_name not in groups:
            print("This group does not exist, create it first!")

        else:
            groups[group_name].add_new_album()

    elif user_choice == 3:
        group_name = input("Enter group name: ")

        groups[group_name] = Group(group_name)
        groups[group_name].load_data_json()

    elif user_choice == 4:
        group_name = input("Enter group name: ")

        groups[group_name] = Group(group_name)
        groups[group_name].load_data_pickle()

    elif user_choice == 5:
        for g in groups.values():
            g.save_data_json()

    elif user_choice == 6:
        for g in groups.values():
            g.save_data_pickle()

    elif user_choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")