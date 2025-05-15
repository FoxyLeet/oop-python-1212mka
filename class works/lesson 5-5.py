try:
    temperatureC = float(input("Введіть температуру в Цельсіях: "))
    degreeF = float(input("Введіть градус фаренгейту: "))
    temperatureF = temperatureC * degreeF
    print(f"Температура в Фаренгейтах: {temperatureF}")


finally:
    print("Дякую, що обираєте нас!")