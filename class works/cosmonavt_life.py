from random import *
class Kosmonavt:

    def __init__(self, name):

        self.name = name
        self.health = 100
        self.energy = 50
        self.moral = 50
        self.alive = True

    def to_explore(self):
        print("Time to explore new planet!")
        self.moral += 5
        self.energy -= 0.12
        chance_trauma = randint(1,5)
        if chance_trauma == 1:
            self.health -= 20
        else:
            print("Expedition went well!")

    def to_repair(self):
            print("Gotta reapir my base!")
            self.moral -= 5
            self.energy -= 7

    def to_rest(self):
        print("Rest time!")
        self.energy = 50
        self.moral += 1
        self.health += 5

    def to_communicate(self):
        print("Finally some chat!")
        self.energy = 50
        self.moral += 0.12
        self.health += 3

    def is_alive(self):

        if self.health <= - 0:
            print("NO WAY I'M DEAD...")
            self.alive = False

        elif self.energy < 0:
            print("I have no energy left...")
            self.alive = False

        elif self.moral < 0:
            print("What's the sense of life...?")
            self.alive = False

    def end_of_day(self, day):
        print("\n")
        print()
        print("-" * 20)
        print(f"Num of the day: {day}")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        print(f"Moral: {self.moral}")
        print("-" * 20)
        print()
        print("\n")



    def live(self, day):

        live_cube = randint(1,3)
        # live_cube = int(input("Enter your choice 1 - study \n2 - sleep \n3 - rest"))

        if live_cube == 1:
            self.to_explore()

        elif live_cube == 2:
                self.to_repair()

        elif live_cube == 3:
            self.to_rest()

        elif live_cube == 3:
            self.to_communicate()

        self.end_of_day(day)
        self.is_alive()


Kosmonavt_kizyak = Kosmonavt("Anton")

for day in range(1,365):

    if Kosmonavt_kizyak.alive == False:
        break

    Kosmonavt_kizyak.live(day)