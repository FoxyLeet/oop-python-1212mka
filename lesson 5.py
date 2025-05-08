"""
try:
    number = int(input("Введіть ціле число: "))

except:
   print("Помилка! Це не ціле число 🙄🙄")

else:
    print(f"Ви ввели число: {number}")

finally:
    print("Кінець програми")
"""


# код який може викликати помилку
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))

    result = a / b

# обробка помилки, винятку
except ZeroDivisionError:
    print("Помилка, на нуль ділити не можна, пупсік...")

except ValueError:
    print("Брух, це не ціле число, мабой ...")

# код який виконується якщо помилки нема
else:
    print(f"Результат ділення: {result}")


finally:
    print("Дякую за використання програми!")