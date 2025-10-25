# Модуль 14. Мережеве програмування
# Тема: Мережеве програмування. Частина 2
#===============================================================================================
# Завдання 1
# Напишіть сервер для збереження даних про фільми.
# Дані знаходяться у файлі films.json
# Напишіть модель на pydentic з такими даними:
# ● id
# ● title
# ● director
# ● year
# Функціонал:
# 1. Отримання даних за ID фільму
# шлях – movies/{movie_id}
# метод – GET
# 2. Додавання нового фільму
# шлях – movies
# метод – POST
# 3. Видалення фільму за ID
# шлях – movies/{movie_id}
# метод – DELETE
# Запустіть сервер
# Напишіть клієнта з таким фуннкціоналом для користувача:
# ● отримати дані про фільм
# ● додати новий фільм
# ● видалити фільм
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os


class Film(BaseModel):
    id: int
    title: str
    director: str
    year: int


app = FastAPI()
FILENAME = "films.json"

@app.get("/movies")
def get_all_movies():
    if not os.path.exists(FILENAME):
        raise HTTPException(status_code=404, detail="No films in database")

    with open(FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

        if len(data) != 0:
            return data
        else:
            return "No films in database"


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    if not os.path.exists(FILENAME):
        raise HTTPException(status_code=404, detail="No films in database")

    else:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)

    key = str(movie_id)

    if key not in data:
        raise HTTPException(status_code=404, detail="Film is not found")

    return data[key]


@app.post("/movies")
def add_new_movie(movie_data: Film):
    if not os.path.exists(FILENAME):
        data = {}

    else:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)

    key = str(movie_data.id)

    if key in data:
        raise HTTPException(status_code=400, detail="Film with this ID is already exists")

    data[key] = movie_data.dict()

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return {"message": "Film is added successfully"}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    if not os.path.exists(FILENAME):
        raise HTTPException(status_code=404, detail="No films in database")

    with open(FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    key = str(movie_id)

    if key not in data:
        raise HTTPException(status_code=404, detail="Film with this ID is not found")

    data.pop(key)

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return {"message": "Film is deleted successfully"}