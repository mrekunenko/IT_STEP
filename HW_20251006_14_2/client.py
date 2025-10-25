import requests


while True:
    user_choice = int(input("Choose service: Get film data(1). "
                            "Get all films from database(2). Add new film(3). "
                            "Delete film(4). Exit(5): "))

    if user_choice == 1:
        film_id = int(input("Enter film ID: "))
        response = requests.get(f"http://localhost:8000/movies/{film_id}")

        if response.ok:
            data = response.json()

            print(f"Movie ID: {data["id"]}. Movie data: {data}")

        else:
            print(response.text)

    elif user_choice == 2:
        response = requests.get(f"http://localhost:8000/movies")

        if response.ok:
            data = response.json()

            for key, value in data.items():
                print(f"Movie ID: {key}. Movie data: {value}")

        else:
            print(response.text)

    elif user_choice == 3:
        film_id = int(input("Enter film ID: "))
        film_title = input("Enter film Title: ")
        film_director = input("Enter film Director: ")
        film_year = int(input("Enter film Year: "))

        film_data = {
            "id": film_id,
            "title": film_title,
            "director": film_director,
            "year": film_year
        }

        response = requests.post(f"http://localhost:8000/movies", json=film_data)

        if response.ok:
            print(response.text)

        else:
            print(response.status_code)

    elif user_choice == 4:
        film_id = int(input("Enter film ID: "))

        response = requests.delete(f"http://localhost:8000/movies/{film_id}")

        if response.ok:
            print(response.text)

        else:
            print(response.text)

    elif user_choice == 5:
        print("Exit from program...")
        break