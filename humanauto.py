class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self, human):
        self.passenger.append(human)

    def print_passenger(self):
        if self.passenger != []:
            print(f"Names of {self.brand} passengers")

            for passenger in self.passenger:
                print(passenger.name)

        else:
                print(f"There are no passengers in {self.brand}")

#Human
Nazar = Human("Nazar")
Maks = Human("Maks")
Ruslanpotuzhnist = Human("Potuzhnist")
Evelinapotuzhna = Human("Potuzhna")
Dimabarabas = Human("Barabas")
Nikita = Human("Nikita")

#Auto
bus_bogdan = Auto("Bogdan Bus")

bus_bogdan.add_passenger(Nazar)
bus_bogdan.add_passenger(Maks)
bus_bogdan.add_passenger(Ruslanpotuzhnist)
bus_bogdan.add_passenger(Evelinapotuzhna)
bus_bogdan.add_passenger(Dimabarabas)
bus_bogdan.add_passenger(Nikita)

bus_bogdan.print_passenger()