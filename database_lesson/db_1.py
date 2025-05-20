# імпортуємо бібліотеку бази даних
import sqlite3

# підключення або створення бази даних
conn = sqlite3.connect("school.db")

# для виконання запитів
cursor = conn.cursor()


# створення таблиці, якщо вона ще не створена
cursor.execute('''       
   CREATE TABLE IF NOT EXISTS students(                    
   id INTEGER PRIMARY KEY,                     
   name TEXT NOT NULL,
   age INTEGER,
   grade TEXT )
   ''')

# підтвердити зміни
conn.commit()

# додавання інформації у таблицю - INSERT INTO
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Руслан", 13, "7-Б"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Евеліна", 13, "7-А"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Назар", 21, "502"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Нікіта", 14, "8-А"))

# підтвердити зміни
conn.commit()

# Зчитування даних

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)


print("ДОДАТКОВО")

cursor.execute("SELECT name FROM students WHERE grade = '7-А' ")
rows = cursor.fetchall()

for row in rows:
    print(row)



# оновлення даних
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("8-Б", "Руслан"))
print("ОНОВЛЕННЯ ДАНИХ")

cursor.execute("SELECT * FROM students ")
rows = cursor.fetchall()
for row in rows:
    print(row)


# Видалення даних
cursor.execute("DELETE FROM students WHERE name = ?", ("Нікіта",))
conn.commit()


print("ПІСЛЯ ВИДАЛЕННЯ")

cursor.execute("SELECT * FROM students ")
rows = cursor.fetchall()
for row in rows:
    print(row)




# видалення значень у таблиці
cursor.execute("DELETE FROM students")
conn.commit()

# завершити зєднання
conn.close()