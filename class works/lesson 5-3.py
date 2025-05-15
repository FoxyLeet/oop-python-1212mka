class NegativeValueError(Exception):
    pass



try:
    amount = float(input("Введіть суму гривень: "))

    if amount < 0:
        raise NegativeValueError("Сума не може бути відємною")

    exchange_rate = int(input("Введіть курс долару: "))
    total = amount / exchange_rate
    print(f"Загальна сума: {total} доларів")

except ValueError:
    print("Помилка! Гроші це числа, геній!")

except ZeroDivisionError:
    print("Помилка! Курс обмінути не може бути 0")

except NegativeValueError as e:
    print(f"Помилка: {e}")


finally:
    print("Дякую, що обираєте нас!")