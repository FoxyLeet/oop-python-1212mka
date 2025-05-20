# імпортуємо бібліотеку бази даних
import sqlite3

# підключення або створення бази даних
conn = sqlite3.connect("library.db")

# для виконання запитів
cursor = conn.cursor()


# створення таблиці, якщо вона ще не створена
cursor.execute('''       
   CREATE TABLE IF NOT EXISTS books(                    
   id INTEGER PRIMARY KEY,                     
   title TEXT NOT NULL,
   author TEXT NOT NULL,
   year INTEGER,
   genre TEXT )
   ''')

# підтвердити зміни
conn.commit()

# додавання інформації у таблицю - INSERT INTO
cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)", ("Чарлі і Шоколадна фабрика", "Роальд Дал", 1964, "казка"))
cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)", ("Магічна Битва", "Геге Акутамі", 2018, "манга"))
cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)", ("Гаррі Поттер", "Джоан Роулінг", 1997, "фентезі"))
cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)", ("Мясник та Чорна пташка", "Брінн Вівер", 2023, "роман"))

# підтвердити зміни
conn.commit()

# Зчитування даних

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)


print("ДОДАТКОВО")

cursor.execute("SELECT title FROM books WHERE author = 'Геге Акутамі' ")
rows = cursor.fetchall()

for row in rows:
    print(row)



# оновлення даних
cursor.execute("UPDATE books SET genre = ? WHERE genre = ?", ("казка", "Чарлі і Шоколадна фабрика"))
print("ОНОВЛЕННЯ ДАНИХ")

cursor.execute("SELECT * FROM books ")
rows = cursor.fetchall()
for row in rows:
    print(row)


# Видалення даних
cursor.execute("DELETE FROM books WHERE title = ?", ("Мясник та Чорна пташка",))
conn.commit()


print("ПІСЛЯ ВИДАЛЕННЯ")

cursor.execute("SELECT * FROM books ")
rows = cursor.fetchall()
for row in rows:
    print(row)




# видалення значень у таблиці
cursor.execute("DELETE FROM books")
conn.commit()

# завершити зєднання
conn.close()