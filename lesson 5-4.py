class NegativeValueError(Exception):
    pass



try:

    age = float(input("Введіть свій вік: "))

    if age <= 0 or age >= 120:
        raise NegativeValueError("Вам не може бути 0 або 120")

    name = input("Введіть своє ім'я: ")

    print(f"Загальна інформація: ім'я - {name}; вік {name} - {age}")

except ValueError:
    print("Помилка! З яких пір у нас вік це будь-що крім числа?")

except NegativeValueError:
    print("Шо ти наш розводиш. Введи справжній вік!")

finally:
    print("Дякую, що обираєте нас!")