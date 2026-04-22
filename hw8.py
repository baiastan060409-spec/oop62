import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

# ЧАСТЬ 1 — СОЗДАНИЕ ТАБЛИЦ

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
""")

conn.commit()


users = [("Ali",), ("Bek",), ("Dana",), ("Aida",), ("Nursultan",)]
movies = [
    ("Inception", "Sci-Fi"),
    ("Titanic", "Drama"),
    ("Avatar", "Fantasy"),
    ("Matrix", "Sci-Fi"),
    ("Joker", "Drama")
]

reviews = [
    (1, 1, 9), (2, 1, 8),
    (3, 2, 7), (4, 2, 9),
    (5, 3, 10), (1, 3, 8),
    (2, 4, 9), (3, 4, 7),
    (4, 5, 8), (5, 5, 9)
]

cursor.executemany("INSERT INTO users (name) VALUES (?)", users)
cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", movies)
cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", reviews)

conn.commit()

# ЧАСТЬ 2 — JOIN

print("\n Пользователь, Фильм, Оценка")

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row)


print("\n ВСЕ фильмы (без отзывов):")

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)

#  ЧАСТЬ 3 — АГРЕГАЦИИ

cursor.execute("SELECT AVG(rating) FROM reviews")
print("\n Средняя оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MAX(rating) FROM reviews")
print(" Максимальная оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MIN(rating) FROM reviews")
print(" Минимальная оценка:", cursor.fetchone()[0])

conn.close()