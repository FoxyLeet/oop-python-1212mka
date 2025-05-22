# імпортуємо бібліотеку бази даних
import sqlite3

# підключення або створення бази даних
conn = sqlite3.connect("stbook.db")

# для виконання запитів
cursor = conn.cursor()


# створення таблиці, якщо вона ще не створена
cursor.execute('''       
   CREATE TABLE IF NOT EXISTS notebooks(                    
   id INTEGER PRIMARY KEY,                     
   subject TEXT,
   owner TEXT,
   pages INTEGER,
   status TEXT )
   ''')

# підтвердити зміни
conn.commit()

# додавання інформації у таблицю - INSERT INTO
cursor.execute("INSERT INTO notebooks (subject, owner, pages, status) VALUES (?, ?, ?, ?)", ("математика", "Максим", 64, "новий"))
cursor.execute("INSERT INTO notebooks (subject, owner, pages, status) VALUES (?, ?, ?, ?)", ("історія", "Евеліна", 24, "заповнений"))
cursor.execute("INSERT INTO notebooks (subject, owner, pages, status) VALUES (?, ?, ?, ?)", ("біологія", "Руслан", 48, "втрачений"))
cursor.execute("INSERT INTO notebooks (subject, owner, pages, status) VALUES (?, ?, ?, ?)", ("англійська", "Нікіта", 18, "язабувдома"))

# підтвердити зміни
conn.commit()

# Зчитування даних

cursor.execute("SELECT * FROM notebooks")
rows = cursor.fetchall()

for row in rows:
    print(row)


print("ДОДАТКОВО")

cursor.execute("SELECT name FROM notebooks WHERE status = 'язабувдома' ")
rows = cursor.fetchall()

for row in rows:
    print(row)



# оновлення даних
cursor.execute("UPDATE notebooks SET pages = ? WHERE owner = ?", (48, "Руслан"))
print("ОНОВЛЕННЯ ДАНИХ")

cursor.execute("SELECT * FROM notebooks ")
rows = cursor.fetchall()
for row in rows:
    print(row)


# Видалення даних
cursor.execute("DELETE FROM notebooks WHERE id = ?", (3,))
conn.commit()


print("ПІСЛЯ ВИДАЛЕННЯ")

cursor.execute("SELECT * FROM notebooks ")
rows = cursor.fetchall()
for row in rows:
    print(row)




# видалення значень у таблиці
cursor.execute("DELETE FROM notebooks")
conn.commit()

# завершити зєднання
conn.close()