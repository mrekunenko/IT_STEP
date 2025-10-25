"""
server.py
Міні API для роботи з фільмами.

Запуск:
    uvicorn server:app --reload
"""

from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from pathlib import Path
import json


# ------------------------
# Data layer helpers
# ------------------------

DATA_FILE = Path("movies.json")


def read_db() -> List[dict]:
    """
    Read the movie database from the JSON file.
    Always returns a list (possibly empty).
    """
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
            if isinstance(data, list):
                return data
            return []
    except json.JSONDecodeError:
        return []


def write_db(movies: List[dict]) -> None:
    """
    Write the movie database (list of dicts) to the JSON file.
    """
    with DATA_FILE.open("w", encoding="utf-8") as fh:
        json.dump(movies, fh, ensure_ascii=False, indent=2)


def find_movie_by_id(movies: List[dict], movie_id: int) -> Optional[dict]:
    """
    Return movie dict with matching id, or None.
    """
    for movie in movies:
        if movie.get("id") == movie_id:
            return movie
    return None


# ------------------------
# Pydantic model
# ------------------------

class Movie(BaseModel):
    """
    Pydantic model for movie validation.
    """
    id: int = Field(..., ge=1, description="Movie unique ID")
    title: str = Field(..., min_length=1, description="Movie title")
    director: str = Field(..., min_length=1, description="Movie director(s)")
    year: int = Field(..., ge=1888, description="Release year (>= 1888)")


# ------------------------
# FastAPI app
# ------------------------

app = FastAPI(
    title="API для фільмів",
    description="Домашнє завдання. Мережеве програмування. Частина 2",
    version="1.2.0",
)


# ------------------------
# Routes
# ------------------------

@app.get("/movies", response_model=List[Movie])
def get_all_movies():
    """
    Get list of all movies.
    Returns [] if empty.
    """
    movies = read_db()
    return movies


@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    """
    Get single movie by ID.
    Raises 404 if not found.
    """
    movies = read_db()
    movie = find_movie_by_id(movies, movie_id)

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Фільм з таким ID не знайдено",
        )

    return movie


@app.post("/movies", response_model=Movie, status_code=status.HTTP_201_CREATED)
def add_movie(new_movie: Movie):
    """
    Add a new movie.
    Raises 400 if ID already exists.
    """
    movies = read_db()

    existing = find_movie_by_id(movies, new_movie.id)
    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Фільм з таким ID вже існує",
        )

    movies.append(new_movie.model_dump())
    write_db(movies)

    return new_movie


@app.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int):
    """
    Delete movie by ID.
    Raises 404 if not found.
    Returns 204 No Content on success.
    """
    movies = read_db()

    updated_movies: List[dict] = []
    found = False

    for movie in movies:
        if movie.get("id") == movie_id:
            found = True
        else:
            updated_movies.append(movie)

    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Фільм для видалення не знайдено",
        )

    write_db(updated_movies)

    return None  # FastAPI will send empty response body with status 204
